/* Public aggregated Cloudflare metrics. No credentials are sent from this page. */
(() => {
  "use strict";
  const box = document.querySelector("[data-cloudflare-stats-url]");
  if (!box) return;
  const url = box.getAttribute("data-cloudflare-stats-url");
  const status = box.querySelector("[data-cloudflare-status]");
  const views = box.querySelector("[data-cloudflare-pageviews]");
  const visits = box.querySelector("[data-cloudflare-visits]");
  const updated = box.querySelector("[data-cloudflare-updated]");
  const unavailable = () => {
    if (status) status.textContent = "Traffic figures currently unavailable";
    if (views) views.textContent = "—";
    if (visits) visits.textContent = "—";
  };
  let target;
  try { target = new URL(url); } catch { unavailable(); return; }
  if (target.protocol !== "https:") { unavailable(); return; }
  const ctl = new AbortController();
  const timeout = setTimeout(() => ctl.abort(), 7000);
  fetch(target.href, { credentials: "omit", mode: "cors", cache: "no-store", signal: ctl.signal })
    .then(r => { if (!r.ok) throw new Error("Unavailable"); return r.json(); })
    .then(data => {
      if (data.available !== true || data.period !== "last_24_hours" ||
          !Number.isSafeInteger(data.pageviews) || !Number.isSafeInteger(data.visits) ||
          data.pageviews < 0 || data.visits < 0) { unavailable(); return; }
      const fmt = new Intl.NumberFormat("en-GB");
      if (views) views.textContent = fmt.format(data.pageviews);
      if (visits) visits.textContent = fmt.format(data.visits);
      if (status) status.textContent = "Recent activity · Cloudflare";
      if (updated && typeof data.updatedAt === "string" && !Number.isNaN(Date.parse(data.updatedAt))) {
        const date = new Date(data.updatedAt);
        updated.dateTime = date.toISOString();
        updated.textContent = "Updated " + date.toLocaleString("en-GB", {
          timeZone: "UTC", day: "numeric", month: "short", hour: "2-digit", minute: "2-digit"
        }) + " UTC.";
      }
    })
    .catch(unavailable)
    .finally(() => clearTimeout(timeout));
})();
