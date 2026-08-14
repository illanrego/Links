#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CSS = ROOT / "styles.css"

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.h1_count = 0
        self.ids: set[str] = set()
        self.hrefs: list[tuple[str, dict[str, str]]] = []
        self.imgs: list[dict[str, str]] = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = {key: value or "" for key, value in attrs}
        self.tags.append((tag, attrs_dict))
        if tag == "h1":
            self.h1_count += 1
        if "id" in attrs_dict:
            self.ids.add(attrs_dict["id"])
        if tag == "a":
            self.hrefs.append((attrs_dict.get("href", ""), attrs_dict))
        if tag == "img":
            self.imgs.append(attrs_dict)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)

html = INDEX.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")
parser = Parser()
parser.feed(html)

if '<html lang="pt-BR"' not in html:
    fail("document language must be pt-BR")
if parser.h1_count != 1:
    fail(f"expected exactly one h1, found {parser.h1_count}")
if not any(href == "#main-content" for href, attrs in parser.hrefs):
    fail("missing skip link to #main-content")
if "main-content" not in parser.ids:
    fail("skip target #main-content missing")
if "href=\"#\"" in html or "href='#'" in html:
    fail("placeholder href found")
if "booking@example.com" in html or "Toda Quinta" in html or "14/6" in html:
    fail("stale placeholder/event copy found")
if "iframe" in html:
    fail("iframe embeds should not be present on the compact links hub")
if "prefers-reduced-motion" not in css:
    fail("missing reduced motion CSS")
if ":focus-visible" not in css:
    fail("missing visible focus CSS")

for href, attrs in parser.hrefs:
    if not href or href.startswith("#") or href.startswith("mailto:"):
        continue
    parsed = urlparse(href)
    if parsed.scheme not in {"http", "https"}:
        fail(f"unexpected href scheme: {href}")
    if attrs.get("target") == "_blank" and attrs.get("rel") != "noreferrer":
        fail(f"external blank target missing rel=noreferrer: {href}")

for attrs in parser.imgs:
    src = attrs.get("src", "")
    alt = attrs.get("alt")
    if alt is None:
        fail(f"image missing alt: {src}")
    if src and not src.startswith(("http://", "https://", "data:")):
        if not (ROOT / src).exists():
            fail(f"missing local image asset: {src}")

for tag, attrs in parser.tags:
    if tag == "link" and attrs.get("href") and not attrs["href"].startswith("http"):
        href = attrs["href"]
        if attrs.get("rel") in {"stylesheet", "icon"} and not (ROOT / href).exists():
            fail(f"missing linked local asset: {href}")

print("static checks passed")
