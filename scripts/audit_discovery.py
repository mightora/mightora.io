#!/usr/bin/env python3
"""Validate published Hugo output and AI discovery feeds without third-party scoring."""
from __future__ import annotations
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = []
        self.in_title = False
        self.description = None
        self.canonical = None
        self.lang = None
        self.h1_count = 0
        self.authors = 0
        self.footers = 0
        self.images = []
        self.structured = []
        self.in_jsonld = False

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "title":
            self.in_title = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = attrs.get("content")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "h1":
            self.h1_count += 1
        if tag == "mightora-author":
            self.authors += 1
        if tag == "mightora-footer":
            self.footers += 1
        if tag == "img" and (attrs.get("src") or "").startswith("/illustrations/"):
            self.images.append(attrs["src"])
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_jsonld = True
            self.structured.append("")

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.in_jsonld:
            self.structured[-1] += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script":
            self.in_jsonld = False


def main():
    records = json.loads((PUBLIC / "tools.json").read_text(encoding="utf-8"))["tools"]
    assert len(records) == 40
    assert len({r["id"] for r in records}) == 40
    assert len({r["name"] for r in records}) == 40
    for record in records:
        for key in ("landingPageUrl", "applicationUrl", "documentationUrl"):
            if record[key] is not None:
                parsed = urlparse(record[key])
                assert parsed.scheme == "https" and parsed.hostname, (record["id"], key)
    llms = (PUBLIC / "llms.txt").read_text(encoding="utf-8")
    assert llms.startswith("# Mightora") and llms.count("](") >= 40
    robots = (PUBLIC / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: https://mightora.io/sitemap.xml" in robots
    assert "Disallow: /" not in robots
    sitemap = ET.parse(PUBLIC / "sitemap.xml").getroot()
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    urls = {e.text for e in sitemap.iter(ns + "loc")}
    assert "https://mightora.io/" in urls, "Homepage absent from sitemap"
    assert "https://mightora.io/catalogue/code-diff/" in urls
    assert "https://mightora.io/catalogue/architecture-lab/" in urls
    html_files = list(PUBLIC.rglob("index.html"))
    assert len(html_files) >= 20, f"Unexpected Hugo build: {len(html_files)} index pages"
    page_reports = []
    for path in html_files:
        parser = PageAudit()
        parser.feed(path.read_text(encoding="utf-8"))
        # Skip generated legacy redirects and aliases. They are not canonical content pages.
        if not parser.canonical or parser.canonical not in urls:
            continue
        assert parser.lang and parser.lang.lower().startswith("en"), path
        assert parser.title and "".join(parser.title).strip(), path
        assert parser.description and len(parser.description.strip()) >= 20, path
        assert parser.canonical.startswith("https://mightora.io/"), path
        assert parser.authors == 1, (path, parser.authors)
        assert parser.footers == 1, (path, parser.footers)
        for src in parser.images:
            assert (PUBLIC / src.lstrip("/")).is_file(), (path, src)
        assert parser.structured, f"Missing JSON-LD: {path}"
        for raw in parser.structured:
            assert isinstance(json.loads(raw), dict), path
        page_reports.append((path.relative_to(PUBLIC).as_posix(), parser.h1_count))
    assert len(page_reports) >= 20, page_reports
    homepage = (PUBLIC / "index.html").read_text(encoding="utf-8")
    assert homepage.index('id="power-platform"') < homepage.index('id="power-bi"')
    assert "mt-tool-guides" in homepage
    assert "mt-document-illustration" in (
        PUBLIC / "catalogue" / "code-diff" / "index.html").read_text(encoding="utf-8")
    print(f"PASS: {len(page_reports)} canonical HTML pages have metadata, JSON-LD, footer and author")
    print(f"PASS: {len(records)} tools, discovery feeds and sitemap coverage")
    uneven = [p for p, n in page_reports if n != 1]
    if uneven:
        print("REVIEW: H1 count is not exactly one on", ", ".join(uneven[:20]))


if __name__ == "__main__":
    main()
