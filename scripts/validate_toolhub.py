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
external = [u for u in urls if u.startswith("https://")]
local = [u for u in urls if u.startswith("/tools/")]

expected_hosts = {
    "power-bi-diff", "semantic-model", "powerbi-inspector", "dax",
    "solution-explorer", "rest", "fetchflow", "expression-lab", "har",
    "architecture-lab", "code-diff", "qr", "radar", "connect",
    "roadmaps", "beta.slides", "feedback",
}
actual_hosts = {urlparse(url).hostname.removesuffix(".mightora.io") for url in external}
assert actual_hosts == expected_hosts, f"Unexpected/missing apps: {actual_hosts ^ expected_hosts}"
assert len(external) == 17, f"Expected 17 hosted apps, got {len(external)}"
assert len(local) == 16, f"Expected 16 documented tools, got {len(local)}"
assert len(urls) == len(names) == 33, (len(urls), len(names))
assert len(set(urls)) == len(set(names)) == 33, "Duplicate tool links or names"
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
assert "33 tools" in template and "8 categories" in template
assert 'hasPrefix .url "https://"' in template
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

print("PASS: 33 unique tools (17 apps + 16 documentation pages), 8 categories, one catalogue")
