#!/usr/bin/env python3
"""Verify Hugo renders each unique catalogue card exactly once on both public pages."""
from html.parser import HTMLParser
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = (root / "data/toolhub.yaml").read_text(encoding="utf-8")
expected = re.findall(r"^        url:\s+(\S+)\s*$", source, re.M)
assert len(expected) == 40

class ToolCards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attrs = dict(attrs)
        if "mt-tool" in (attrs.get("class") or "").split():
            self.urls.append(attrs.get("href"))

for page in (root / "public/index.html", root / "public/tools/index.html"):
    assert page.is_file(), f"Missing Hugo output: {page}"
    parser = ToolCards()
    parser.feed(page.read_text(encoding="utf-8"))
    assert len(parser.urls) == len(expected), (
        f"{page}: expected {len(expected)} cards, got {len(parser.urls)}"
    )
    assert sorted(parser.urls) == sorted(expected), (
        f"{page}: missing {set(expected) - set(parser.urls)}, "
        f"unexpected {set(parser.urls) - set(expected)}"
    )
    print(f"PASS: {page.relative_to(root)} has all 40 unique resource cards")

# Use HTMLParser: Hugo minification may remove quotes from class attributes.
class MetricNumbers(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = []
        self.in_number = False

    def handle_starttag(self, tag, attrs):
        self.in_number = tag == "span" and "mt-site-metric-number" in dict(attrs).get("class", "").split()

    def handle_data(self, data):
        if self.in_number:
            self.values.append(int(data.strip()))

    def handle_endtag(self, tag):
        if tag == "span":
            self.in_number = False

html = (root / "public/index.html").read_text(encoding="utf-8")
assert "mt-site-metrics-grid" in html, "Missing homepage statistics section"
metric_parser = MetricNumbers()
metric_parser.feed(html)
assert metric_parser.values == [40, 18, 16, 6, 8], (
    f"Unexpected derived homepage figures: {metric_parser.values}"
)
assert "mt-cloudflare-stats" not in html, "Cloudflare panel should be hidden until endpoint is configured"
print("PASS: homepage has correct catalogue statistics and no unconfigured visitor data")
