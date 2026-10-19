#!/usr/bin/env python3
"""Produce local lightweight SVG diagrams for every Hugo Markdown page.

Deterministic generation keeps the illustrations aligned with the content tree.
No stock artwork, remote images or third-party image services are used.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
DEST = ROOT / "static" / "illustrations" / "pages"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def illustration_key(path: Path) -> str:
    relative = path.relative_to(CONTENT)
    base = relative.parent.as_posix() if path.stem == "_index" else relative.with_suffix("").as_posix()
    return slug(base)


def title_from_frontmatter(source: str, fallback: str) -> str:
    match = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", source, re.M)
    return match.group(1).strip().strip('"').strip("'") if match else fallback.replace("-", " ").title()


def diagram(title: str, key: str) -> str:
    palettes = [
        ("#0c4a46", "#34d399", "#a7f3d0"),
        ("#113a50", "#60a5fa", "#bae6fd"),
        ("#43316c", "#a78bfa", "#ddd6fe"),
        ("#64441a", "#fbbf24", "#fde68a"),
    ]
    digest = hashlib.sha256(key.encode()).digest()
    background, primary, pale = palettes[digest[0] % len(palettes)]
    nodes = 3 + digest[1] % 3
    shapes = []
    coords = [(72, 100), (215, 65), (355, 104), (495, 70), (572, 130)]
    for index in range(nodes):
        x, y = coords[index]
        if index:
            px, py = coords[index - 1]
            shapes.append(f'<path d="M{px+38} {py+17} Q{(px+x)//2} {py-8} {x-38} {y+17}" stroke="{pale}" stroke-width="3" stroke-dasharray="8 6" opacity=".8"/>')
        kind = (digest[index + 2] % 3)
        if kind == 0:
            shapes.append(f'<rect x="{x-36}" y="{y-23}" width="72" height="46" rx="12" stroke="{primary}" fill="#ffffff" fill-opacity=".08" stroke-width="3"/>')
        elif kind == 1:
            shapes.append(f'<circle cx="{x}" cy="{y}" r="30" stroke="{primary}" fill="#ffffff" fill-opacity=".07" stroke-width="3"/>')
        else:
            shapes.append(f'<path d="M{x} {y-31}L{x+34} {y}L{x} {y+31}L{x-34} {y}Z" stroke="{primary}" fill="#ffffff" fill-opacity=".07" stroke-width="3"/>')
        shapes.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{pale}"/>')
    label = escape(title[:64])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" role="img" aria-labelledby="title desc">
<title id="title">{label} — architecture illustration</title>
<desc id="desc">An original sequence of connected technical components illustrating {label}.</desc>
<rect width="680" height="220" rx="20" fill="{background}"/>
<path d="M0 175H680 M0 35H680" stroke="#ffffff" stroke-opacity=".10"/>
<g>{''.join(shapes)}</g>
<text x="35" y="193" fill="#ffffff" font-family="system-ui,sans-serif" font-size="18" font-weight="650">{escape(title[:53])}</text>
</svg>\n'''


def main() -> None:
    pages = list(CONTENT.rglob("*.md"))
    DEST.mkdir(parents=True, exist_ok=True)
    count = 0
    for page in pages:
        key = illustration_key(page)
        if not key:  # Home already has a detailed bespoke vector.
            continue
        source = page.read_text(encoding="utf-8")
        title = title_from_frontmatter(source, page.stem)
        (DEST / f"{key}.svg").write_text(diagram(title, key), encoding="utf-8")
        count += 1
    print(f"PASS: generated {count} local, content-specific SVG illustrations")


if __name__ == "__main__":
    main()
