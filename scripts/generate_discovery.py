#!/usr/bin/env python3
"""Build honest, deterministic agent-discovery artefacts from data/toolhub.yaml.

Run after the production Hugo build. No network calls or guessed application facts.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://mightora.io"
OUTPUT = ROOT / "public"
CATALOGUE = ROOT / "data" / "toolhub.yaml"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build() -> list[dict]:
    groups = yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))["groups"]
    records = []
    seen_ids = set()
    for group in groups:
        for entry in group["tools"]:
            identifier = slugify(entry["name"])
            assert identifier not in seen_ids, f"Duplicate catalogue identifier: {identifier}"
            seen_ids.add(identifier)
            url = entry["url"]
            external = url.startswith("https://")
            assert external or url.startswith("/tools/"), url
            if external:
                address = urlparse(url)
                assert address.hostname and address.hostname.endswith(".mightora.io"), url
            curated = ROOT / "content" / "catalogue" / identifier / "_index.md"
            page = f"{SITE}/catalogue/{identifier}/" if curated.is_file() else (
                url if external else f"{SITE}{url}")
            docs = (f"{SITE}/catalogue/{identifier}/" if curated.is_file() else
                    (f"{SITE}{url}" if not external else None))
            record = {
                "id": identifier, "name": entry["name"],
                "description": entry["description"], "category": group["title"],
                "categoryId": group["id"], "landingPageUrl": page,
                "applicationUrl": url if external else None,
                "documentationUrl": docs, "sourceRepositoryUrl": None,
                "license": None, "isFree": None, "requiresInstallation": (
                    False if external else None),
                "browserRequirements": "Modern web browser" if external else None,
                "supportedInputs": None, "supportedOutputs": None,
                "offlineCapable": None, "authenticationRequired": None,
                "dataProcessingModel": None,
                "status": "sample" if entry.get("kind") == "sample" else "unverified",
                "kind": "sample" if entry.get("kind") == "sample" else (
                    "browser-app" if external else "documentation"),
                "tags": [group["id"]], "useCases": [entry["description"]],
            }
            records.append(record)
    return records


def publish() -> None:
    if not (OUTPUT / "index.html").exists():
        raise SystemExit("Hugo must build public/index.html before discovery generation.")
    records = build()
    OUTPUT.mkdir(exist_ok=True)
    payload = {
        "schemaVersion": "1.0", "publisher": "Mightora",
        "siteUrl": SITE + "/", "licensingNote": (
            "Check each project's repository for its licence. No per-tool licence, "
            "data-handling or authentication claims are inferred."),
        "tools": records,
    }
    (OUTPUT / "tools.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Mightora", "",
        "> A catalogue of developer resources for Power Platform, architecture, "
        "automation, DevOps and diagnostics.", "",
        "The catalogue distinguishes live browser apps, documentation and "
        "connector samples. Availability, data processing, authentication and "
        "licensing depend on each individual project and must be checked separately.", "",
        "## Directory and documentation", "",
        "- [All tools](https://mightora.io/tools/)",
        "- [Tool catalogue as JSON](https://mightora.io/tools.json)",
        "- [About Mightora](https://mightora.io/about/)", "",
    ]
    for category in dict.fromkeys(r["category"] for r in records):
        category_records = [r for r in records if r["category"] == category]
        lines += [f"## {category}", ""]
        for record in category_records:
            lines.append(f"- [{record['name']}]({record['landingPageUrl']}): "
                         f"{record['description']}")
        lines.append("")
    lines += [
        "## Source and limitations", "",
        "- [Mightora GitHub organisation](https://github.com/mightora)",
        "- [Website source](https://github.com/mightora/mightora.io)",
        "- [Privacy information](https://mightora.io/privacy/)", "",
        "This is an emerging AI-reader convention, not an indexing or ranking guarantee.",
        "Some tools are independently hosted on Mightora subdomains, not on this website.", "",
    ]
    (OUTPUT / "llms.txt").write_text("\n".join(lines), encoding="utf-8")
    # No explicit GPTBot permission change. The owner may choose separate training policy.
    (OUTPUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://mightora.io/sitemap.xml\n",
        encoding="utf-8")
    print(f"PASS: generated discovery feeds for {len(records)} verified catalogue entries")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--validate":
        assert len(build()) == 40
        print("PASS: 40 unique valid catalogue entries")
    else:
        publish()
