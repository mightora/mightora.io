# Cloudflare Web Analytics on Mightora

This optional Cloudflare Worker publishes only **24-hour page views and visits** for `mightora.io`. It reads Cloudflare's RUM (browser analytics) events and caches results for 15 minutes. It does not disclose personal visitor data or the Cloudflare API token.

The Mightora site is hosted on GitHub Pages, so an authenticated Cloudflare Analytics API call must run outside the browser. **There is no direct API call or credential embedded in the site.**

## Enable the visitor statistics

Cloudflare's Web Analytics beacon is already present in `layouts/partials/head.html`. This Worker is intentionally not deployed or enabled by default.

1. Create a *scoped*, read-only Cloudflare API token with **Account → Analytics → Read** permission for the account that owns `mightora.io`.
2. From this directory, authenticate with `npx wrangler login`.
3. Set Worker secrets using `npx wrangler secret put CF_API_TOKEN`, `npx wrangler secret put CF_ACCOUNT_TAG`, `npx wrangler secret put CF_SITE_TAG`, and `npx wrangler secret put CF_HOSTNAME`. Enter `mightora.io` for the hostname and obtain the account and site tags from your account.
4. Deploy using `npx wrangler deploy`. Check the deployed HTTPS `/metrics` route. If Cloudflare has no RUM records, it will return `available: false` instead of a misleading zero.
5. Set `params.cloudflareStats.endpoint` in the site's `hugo.yaml` to your Worker's `https://...workers.dev/metrics` URL. Deploy the site. Only then will the Cloudflare metrics panel appear.

Never commit the token, publish it to browser code, or use broad API permissions. To hide all visitor figures, keep the endpoint empty.

## Data limitations

- Page views and visits are aggregated browser RUM measurements for the `mightora.io` hostname, not all requests across Mightora subdomains.
- The Worker returns only aggregate counts and a freshness timestamp.
- The metrics are cached for 15 minutes and do not form a real-time visitor counter.
- On upstream failure, missing credentials, or absent records, the frontend shows an unavailable state, not invented counts.
- This integration does not modify Cloudflare DNS settings or proxy mode.
