/**
 * Public 24-hour Cloudflare RUM aggregates. Secrets are Cloudflare Worker bindings,
 * never GitHub repo variables or frontend content.
 */
const API = "https://api.cloudflare.com/client/v4/graphql";
const ORIGINS = new Set(["https://mightora.io", "https://www.mightora.io"]);
const CACHE_SECONDS = 900;
const QUERY = [
  "query SiteMetrics($accountTag: string!, $siteTag: string!, $host: string!, $start: Time!, $end: Time!) {",
  "  viewer { accounts(filter: { accountTag: $accountTag }) {",
  "    rumPageloadEventsAdaptiveGroups(limit: 1, filter: {",
  "      siteTag: $siteTag, requestHost: $host, datetime_geq: $start, datetime_lt: $end",
  "    }) { count sum { visits } }",
  "  } }",
  "}",
].join("\n");

function responseJSON(payload, status, origin, cacheSeconds = 0) {
  const headers = {
    "Content-Type": "application/json; charset=utf-8",
    "X-Content-Type-Options": "nosniff",
    "Cache-Control": cacheSeconds ? "public, max-age=60, s-maxage=" + cacheSeconds : "no-store",
    "Vary": "Origin",
  };
  if (ORIGINS.has(origin)) {
    headers["Access-Control-Allow-Origin"] = origin;
    headers["Access-Control-Allow-Methods"] = "GET, OPTIONS";
  }
  return new Response(JSON.stringify(payload), { status, headers });
}

export default {
  async fetch(request, env, ctx) {
    const origin = request.headers.get("Origin") || "";
    if (origin && !ORIGINS.has(origin)) return responseJSON({ available: false }, 403, origin);
    if (request.method === "OPTIONS") return new Response(null, {
      status: 204,
      headers: {
        "Access-Control-Allow-Origin": origin || "https://mightora.io",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Vary": "Origin",
      },
    });
    if (request.method !== "GET") return responseJSON({ available: false }, 405, origin);
    if (!["/", "/metrics"].includes(new URL(request.url).pathname)) {
      return responseJSON({ available: false }, 404, origin);
    }
    if (!env.CF_API_TOKEN || !env.CF_ACCOUNT_TAG || !env.CF_SITE_TAG || !env.CF_HOSTNAME) {
      return responseJSON({ available: false, error: "Not configured" }, 503, origin);
    }
    const cache = caches.default;
    const key = new Request("https://internal-metrics.mightora.invalid/rum24h");
    const hit = await cache.match(key);
    if (hit) return responseJSON(await hit.json(), 200, origin, CACHE_SECONDS);
    try {
      const end = new Date(), start = new Date(end.getTime() - 86400000);
      const upstream = await fetch(API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + env.CF_API_TOKEN,
        },
        body: JSON.stringify({
          query: QUERY,
          variables: {
            accountTag: env.CF_ACCOUNT_TAG,
            siteTag: env.CF_SITE_TAG,
            host: env.CF_HOSTNAME,
            start: start.toISOString(),
            end: end.toISOString(),
          },
        }),
      });
      if (!upstream.ok) throw new Error("Upstream error");
      const body = await upstream.json();
      if (body.errors?.length) throw new Error("GraphQL error");
      const groups = body?.data?.viewer?.accounts?.[0]?.rumPageloadEventsAdaptiveGroups;
      if (!Array.isArray(groups)) throw new Error("Unexpected data shape");
      const row = groups[0];
      // Empty data does not prove zero visitors.
      if (!row || !Number.isSafeInteger(row.count) || !Number.isSafeInteger(row.sum?.visits)) {
        return responseJSON({ available: false, period: "last_24_hours" }, 200, origin);
      }
      const summary = {
        available: true,
        source: "Cloudflare Web Analytics",
        period: "last_24_hours",
        pageviews: row.count,
        visits: row.sum.visits,
        updatedAt: end.toISOString(),
      };
      ctx.waitUntil(cache.put(key, responseJSON(summary, 200, "", CACHE_SECONDS)));
      return responseJSON(summary, 200, origin, CACHE_SECONDS);
    } catch {
      return responseJSON({ available: false, error: "Metrics unavailable" }, 503, origin);
    }
  },
};
