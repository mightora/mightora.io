# Mightora website catalogue, SEO and agent-discovery maintenance

The site is built with Hugo/Hextra and published to GitHub Pages. Keep this architecture: no backend service is required.

## Add or update a tool

1. Edit **data/toolhub.yaml**. Choose one of the existing categories, or add a justified new one. Give the tool a unique, descriptive name, accurate one-sentence purpose and real URL. Browser apps link to their public HTTPS Mightora subdomain. Existing Markdown tools link to their local /tools/... page.
2. If the tool needs its own explanatory page, add **content/catalogue/<tool-slug>/_index.md**. Explain the problem, audience, example use, limitations and the exact launch URL. Do not claim an offline edition, no data transfer, licence or account-free access unless verified.
3. For local docs, keep the actual Markdown source in **content/tools/**. The existing include-processing pipeline is preserved.
4. The homepage, navigation category order, **tools.json**, **llms.txt**, canonical HTML and sitemap derive from the catalogue and/or Hugo content tree. Do not hand-edit generated files in public/.
5. Push a branch and inspect the **Site catalogue checks** result. The checks build Hugo, generate page-specific SVGs, validate existing cards and inspect the resulting metadata, schema, sitemap and feeds. Only publish once checks pass.
6. Confirm live URLs and, for tool-specific factual claims, verify the target app/repository separately. The catalogue schema uses `null` for unknown properties rather than guesses.

## Generated assets

- `scripts/generate_artwork.py` creates lightweight local vector illustrations in `static/illustrations/pages/` based on Markdown page paths and titles, before Hugo builds.
- Hugo renders HTML and its native XML sitemap. `enableGitInfo` uses source history for meaningful last-modified dates rather than a fresh timestamp on every build.
- `scripts/generate_discovery.py` writes `public/tools.json`, `public/llms.txt` and `public/robots.txt` **after** Hugo. It reads only `data/toolhub.yaml`.
- `scripts/audit_discovery.py` inspects published HTML and generated feeds. The catalogue's URLs are validated structurally, not guaranteed live by the offline CI step.

## Metadata and content rules

- Each Markdown page should define an accurate `title` and `description` front matter pair and contain one meaningful H1 (verify the rendered theme output).
- Canonical URLs must match the HTML URL. Use actual direct app URLs for apps hosted on subdomains; a Mightora.io catalogue article is not the app itself.
- The shared head injects Organization, WebSite, CollectionPage/ItemList and WebPage/BreadcrumbList JSON-LD. The catalogue is a navigational directory, not an assertion that every linked application is hosted here.
- Do not add fictitious reviews, scores, licences, number of users, prices, uptime guarantees, security certifications or privacy guarantees.
- Keep helpful content readable without JavaScript. Search crawlers and AI systems need links and explanatory HTML, not instructions intended to bias rankings.

## Indexing and account access

The sitemap is **https://mightora.io/sitemap.xml**. Verify the domain and inspect sitemap indexing in Google Search Console and Bing Webmaster Tools when website-owner access is provided. Search engines decide whether to index; publishing a sitemap or an llms.txt file does not guarantee inclusion.

The generated robots policy allows public crawling. It does **not** contain bot-specific blocks. A site owner must separately decide whether to restrict model-training crawlers such as GPTBot; OAI-SearchBot has a different discovery purpose. Record and review that policy before changing it.

IndexNow is not configured: it requires domain-key ownership and a tested changed-URL submission pipeline. Do not submit all URLs on every scheduled build. Do not claim Google or Bing ownership without verification.

## Shared components

Mightora uses the public `mightora/shared-ui` stylesheet and web components. `js-yaml` must load **before** `components.js`. The footer uses the local synced `/footer.yaml`, preserving the pre-existing shared footer workflow; keep the local fallback within `<mightora-footer>`. Keep the prescribed TechTweedie biography above the footer. Verify CSS, dependency order, offline degradation, mobile and dark mode after changes.

## Release checks

1. Run the project content processors and `python3 scripts/generate_artwork.py`.
2. Run Hugo with `--gc --minify --baseURL https://mightora.io/`.
3. Run `python3 scripts/generate_discovery.py`, `scripts/validate_toolhub.py`, `scripts/check_rendered_toolhub.py` and `scripts/audit_discovery.py`.
4. Confirm deployment through the **Deploy Mightora Website** GitHub Action and inspect `https://mightora.io/tools.json`, `/llms.txt`, `/robots.txt` and `/sitemap.xml`.
5. For performance and accessibility, run Lighthouse and manual keyboard/mobile checks. Numeric Web Vitals and Lighthouse scores require actual measurements, not repository inspection.

## Known follow-up work

- Audit the older FAQ, privacy policy, analytic beacons and externally maintained documentation for current accuracy, lawful basis and dead links.
- Develop unique verified explanatory articles for remaining external tools as research becomes available, rather than manufacturing thin pages.
- Confirm Hextra's `sidebar.hide` behaviour against the pinned theme version: the homepage already uses a dedicated full-width `layouts/index.html`, whereas newer Hextra versions offer an explicit front matter switch.
- Verify individual application repositories and add truthful licence, source, data-handling and auth information to the catalogue only after evidence is available.
- Confirm live performance, mobile interaction and browser-agent tasks using a browser with the necessary environment and account permissions.
