#!/usr/bin/env python3
"""Validate the single data-driven Mightora catalogue without external dependencies."""
from pathlib import Path
from urllib.parse import urlparse
import re

root = Path(__file__).resolve().parents[1]
source = (root / "data/toolhub.yaml").read_text(encoding="utf-8")
template = (root / "layouts/shortcodes/tool-hub.html").read_text(encoding="utf-8")

# Both app URLs and local documentation pages are first-class catalogue entries.
urls = re.findall(r"^        url:\s+(\S+)\s*$", source, re.M)
names = re.findall(r'^      - name:\s+"([^"]+)"\s*$', source, re.M)
external = [u for u in urls if u.startswith("https://") or u == "http://connect.mightora.io/"]
local = [u for u in urls if u.startswith("/tools/")]

expected_hosts = {
    "power-bi-diff", "semantic-model", "powerbi-inspector", "dax",
    "solution-explorer", "rest", "fetchflow", "expression-lab", "har",
    "architecture-lab", "code-diff", "qr", "radar", "connect",
    "roadmaps", "beta.slides", "feedback", "custom-connector-builder",
}
actual_hosts = {urlparse(url).hostname.removesuffix(".mightora.io") for url in external}
assert actual_hosts == expected_hosts, f"Unexpected/missing apps: {actual_hosts ^ expected_hosts}"
# Connect is intentionally plain HTTP to allow Wi-Fi captive portal interception.
# No other public tool may silently move away from HTTPS.
assert source.count("        kind: http-only") == 1
assert "http://connect.mightora.io/" in external
assert "https://connect.mightora.io/" not in source
assert all(
    url == "http://connect.mightora.io/" or url.startswith("https://")
    for url in external
), "All tools except Connect must use HTTPS"
assert 'eq .url "http://connect.mightora.io/"' in template
assert 'eq .kind "http-only"' in template

assert len(external) == 24, f"Expected 24 externally linked resources, got {len(external)}"
assert len(local) == 16, f"Expected 16 documented tools, got {len(local)}"
assert len(urls) == len(names) == 40, (len(urls), len(names))
assert len(set(urls)) == len(set(names)) == 40, "Duplicate tool links or names"
assert len(re.findall(r"^  - id: ", source, re.M)) == 8, "Expected eight categories"
assert "legacy:" not in source, "All tools must be under the same groups key"

for url in local:
    assert (root / "content" / url.strip("/") / "_index.md").is_file(), f"Missing documentation: {url}"
for path in ("content/_index.md", "content/tools/_index.md"):
    content = (root / path).read_text(encoding="utf-8")
    assert content.count("{{< tool-hub >}}") == 1, path
    assert "{{< cards >}}" not in content, f"Duplicate generated cards on {path}"

assert "{{ range $hub.groups }}" in template
assert "{{ range .tools }}" in template
assert "$hub.legacy" not in template
assert 'class="mt-original"' not in template
assert "40 tools" in template and "8 categories" in template
assert 'eq .url "http://connect.mightora.io/"' in template
for label, anchor in (("Build", "power-platform"), ("Inspect", "diagnostics"),
                      ("Architect", "architecture"), ("Deploy", "devops")):
    assert f"<strong>{label}</strong>" in template, label
    assert f'href="#{anchor}"' in template, anchor
for group_id in ("power-bi", "power-platform", "power-automate", "devops", "diagnostics",
                 "architecture", "engagement", "connectivity"):
    assert f"id: {group_id}" in source

assert (root / "data/footer.yaml").read_text() == (root / "static/footer.yaml").read_text()
footer = (root / "layouts/partials/footer.html").read_text()
assert "<mightora-author>" in footer and '<section class="mt-author-wrapper"' in footer
assert "author-avatar" in footer and "author-blog-logo" in footer

sample_slugs = [
    "regex-tester", "markdown-html-converter", "compare-json-lists",
    "business-rules-calculator", "pricing-calculator", "json-calculation-engine",
]
sample_urls = [
    f"https://custom-connector-builder.mightora.io/#/connector/{slug}"
    for slug in sample_slugs
]
assert all(url in external for url in sample_urls), "Missing a connector sample deep link"
assert source.count("        kind: sample") == len(sample_slugs), "Sample count or classification mismatch"
assert 'eq .kind "sample"' in template and "Sample connector" in template
print("PASS: 40 unique resources (18 apps + 6 sample connectors + 16 documentation pages), 8 categories")

# Home-only figures are based on the catalogue rather than manual numbers.
tpl = (root / "layouts/shortcodes/tool-hub.html").read_text(encoding="utf-8")
assert 'if .Page.IsHome' in tpl and 'class="mt-site-metrics"' in tpl
for variable in ("$resources", "$apps", "$docs", "$samples"):
    assert variable in tpl
assert 'site.Params.cloudflareStats.endpoint' in tpl
assert 'data-cloudflare-stats-url' in tpl
base = (root / "layouts/_default/baseof.html").read_text(encoding="utf-8")
style = (root / "assets/css/custom.css").read_text(encoding="utf-8")
assert 'mt-home-page' in base and 'body.mt-home-page .hextra-toc' in style
assert 'mt-site-metrics-grid' in style
frontend = (root / "static/js/cloudflare-stats.js").read_text(encoding="utf-8")
assert 'credentials: "omit"' in frontend
assert "CF_API_TOKEN" not in frontend
worker = (root / "workers/cloudflare-traffic/src/index.mjs").read_text(encoding="utf-8")
assert "CF_API_TOKEN" in worker and "caches.default" in worker
assert "last_24_hours" in worker and "ORIGINS" in worker
print("PASS: homepage tool metrics and optional Cloudflare stats integration")
