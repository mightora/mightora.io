# Mightora unified tool directory

Both the homepage and `/tools/` render **one catalogue** from `data/toolhub.yaml`, using the `tool-hub` shortcode. Every one of the 40 items lives in **one category**, whether it is a standalone static web app at a `*.mightora.io` subdomain or has a documentation page under `/tools/`.

## Adding or editing tools

- Add a single entry within the relevant `groups[].tools` list, with `name`, `description` and `url`.
- For hosted apps, use the full public HTTPS URL, linking directly to the application, not GitHub.
- For connectors, scripts, PCF controls, templates and extensions with Mightora documentation, link to the existing `/tools/...` URL. Do not create duplicate cards elsewhere.
- Do **not** add a separate legacy/original collection. Hosting and documentation do not determine the category.
- To update section titles or order, edit the `groups` list. The quick-jump navigation is generated from those groups.
- The four prominent Build / Inspect / Architect / Deploy shortcuts are helpful entry points to the unified categories; they don't represent separate catalogues.
- `data/footer.yaml` and `static/footer.yaml` must be kept in sync.

## Verification

Run `python3 scripts/validate_toolhub.py`. Pull requests run the full Hugo site build, including the original Markdown include processor and the updater used on individual documentation pages. The generated homepage and `/tools/` page must each contain all 40 unique catalogue cards. GitHub Pages publishes from `main` after validation.

## Custom connector examples

The **Power Automate & connectors** category also includes the public **Custom Connector Builder**, plus each of its six documented sample connectors as an individually labelled **Sample connector** card. These are linked to the application\'s verified hash routes (`/#/connector/<id>`) rather than a general introduction page. They are **examples and walkthroughs**, not separately deployed services.

The six routes follow `CONNECTORS[].id` from `mightora/custom-connector-builder/src/main.js`: `regex-tester`, `markdown-html-converter`, `compare-json-lists`, `business-rules-calculator`, `pricing-calculator`, and `json-calculation-engine`.

When new sample connectors are added to the builder, update this catalogue and the allowlist checks in `scripts/validate_toolhub.py` together.

## Homepage at a glance and Cloudflare analytics

The homepage hides only its right-side Hextra table-of-contents panel; documentation pages retain their navigation. The five headline metrics are generated from `data/toolhub.yaml` at build time (currently 40 resources, 18 standalone browser apps, 16 documented utilities, 6 sample connectors and 8 categories). The homepage figure checks fail the build if the counts become inconsistent.

Cloudflare Web Analytics is already installed on the site. However, live Cloudflare visitor data cannot be fetched with an API token directly from GitHub Pages. An optional read-only, cached Worker is provided in `workers/cloudflare-traffic/`. Until an Analytics Read token is securely stored as a Worker secret and `params.cloudflareStats.endpoint` is configured in `hugo.yaml`, no visitor counts appear. See the Worker README for setup, data boundaries and privacy controls. Neither the Cloudflare API token nor arbitrary analytics records are exposed publicly.
