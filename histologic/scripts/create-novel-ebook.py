#!/usr/bin/env python3
"""
Create EPUB ebooks for the Histologic novels.

Usage: python3 scripts/create-novel-ebook.py [04] [05]   (default: all books)
Books are configured in scripts/novels_config.py.
"""

import os
import re
from pathlib import Path
from datetime import datetime, timezone
import html
import uuid
import zipfile

from novels_config import BOOKS, select_books

AUTHOR = "Histologic Series"
LANGUAGE = "en"


def configure(key):
    """Point the module-level settings at one book from novels_config.BOOKS."""
    global NOVEL_DIR, CHAPTERS_DIR, OUTPUT_FILE, NOVEL_TITLE, NOVEL_SUBTITLE, DESCRIPTION, PARTS, CHAPTERS
    book = BOOKS[key]
    NOVEL_DIR = book["dir"]
    CHAPTERS_DIR = NOVEL_DIR / "chapters"
    OUTPUT_FILE = NOVEL_DIR / book["epub"]
    NOVEL_TITLE = book["title"]
    NOVEL_SUBTITLE = book["subtitle"]
    DESCRIPTION = book["description"]
    PARTS = book["parts"]
    CHAPTERS = [(f, f"{n}: {t}") for _, chs in PARTS for (f, n, t, _pov) in chs]


def clean_content(content):
    """Remove old-style trailing notes and the chapter's own leading heading."""
    content = re.sub(r'\*\*End of Chapter.*', '', content, flags=re.DOTALL)
    content = re.sub(r'---\s*$', '', content, flags=re.DOTALL)
    content = re.sub(r'\A# .*\n', '', content.strip())
    return content.strip()

def inline(text):
    """Escape XML and convert inline markdown (bold, italic)."""
    text = html.escape(text, quote=False)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def markdown_to_html(text):
    """Convert the small markdown subset used by the chapters to XHTML."""
    out = []
    for block in re.split(r'\n\s*\n', text):
        block = block.strip()
        if not block:
            continue
        if block == '---':
            out.append('<hr/>')
        elif block.startswith('### '):
            out.append(f'<h3>{inline(block[4:])}</h3>')
        elif block.startswith('## '):
            out.append(f'<h2>{inline(block[3:])}</h2>')
        elif block.startswith('# '):
            out.append(f'<h1>{inline(block[2:])}</h1>')
        else:
            out.append(f'<p>{inline(" ".join(block.splitlines()))}</p>')
    return '\n'.join(out)

STYLE = """body { font-family: Georgia, serif; line-height: 1.6; margin: 1em; }
h1 { font-size: 1.8em; margin: 1.5em 0 1em; text-align: center; page-break-before: always; }
h2 { font-size: 1.3em; margin: 1.5em 0 0.5em; }
p { text-align: justify; margin: 0 0 0.8em; text-indent: 1.5em; }
h1 + p, hr + p, h2 + p { text-indent: 0; }
hr { border: none; border-top: 1px solid #999; margin: 1.5em 30%; }
.part { text-align: center; margin-top: 30%; font-size: 1.6em; letter-spacing: 0.1em; }
.title { text-align: center; margin-top: 25%; }
.title h1 { page-break-before: auto; font-size: 2.4em; }
.title p { text-align: center; text-indent: 0; }
"""

def xhtml(title, body):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{LANGUAGE}" xml:lang="{LANGUAGE}">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{body}
</body>
</html>
"""

def create_ebook():
    """Create the EPUB ebook (EPUB 3 with an NCX for older readers)."""
    print(f"Creating EPUB ebook for: {NOVEL_TITLE}")
    print(f"Chapters: {len(CHAPTERS)}")
    print()

    book_id = f"urn:uuid:{uuid.uuid4()}"
    items = []      # (id, href, title, content, in_toc)

    items.append(("title", "title.xhtml", NOVEL_TITLE, xhtml(NOVEL_TITLE,
        f'<div class="title"><h1>{html.escape(NOVEL_TITLE)}</h1><p><em>{html.escape(NOVEL_SUBTITLE)}</em></p></div>'), False))

    n = 0
    for part_title, chapters in PARTS:
        if part_title.startswith("Part"):
            pid = f"part{len(items):02d}"
            items.append((pid, f"{pid}.xhtml", part_title,
                          xhtml(part_title, f'<div class="part">{html.escape(part_title)}</div>'), True))
        for filename, num, title, _pov in chapters:
            full_title = f"{num}: {title}"
            print(f"Processing: {full_title}")
            content = clean_content((CHAPTERS_DIR / filename).read_text(encoding="utf-8"))
            body = f"<h1>{html.escape(full_title)}</h1>\n{markdown_to_html(content)}"
            cid = f"chapter{n:02d}"
            items.append((cid, f"{cid}.xhtml", full_title, xhtml(full_title, body), True))
            n += 1

    toc = [i for i in items if i[4]]
    nav_list = "\n".join(f'<li><a href="{href}">{html.escape(t)}</a></li>' for _, href, t, _, _ in toc)
    nav = xhtml("Contents", f'<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>\n{nav_list}\n</ol></nav>')
    ncx_points = "\n".join(
        f'<navPoint id="np{k}" playOrder="{k}"><navLabel><text>{html.escape(t)}</text></navLabel><content src="{href}"/></navPoint>'
        for k, (_, href, t, _, _) in enumerate(toc, 1))
    ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{book_id}"/></head>
<docTitle><text>{html.escape(NOVEL_TITLE)}</text></docTitle>
<navMap>
{ncx_points}
</navMap>
</ncx>
"""
    manifest = "\n".join(f'<item id="{i}" href="{h}" media-type="application/xhtml+xml"/>' for i, h, _, _, _ in items)
    spine = "\n".join(f'<itemref idref="{i}"/>' for i, _, _, _, _ in items)
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title>{html.escape(NOVEL_TITLE)}</dc:title>
<dc:creator>{html.escape(AUTHOR)}</dc:creator>
<dc:language>{LANGUAGE}</dc:language>
<dc:description>{html.escape(DESCRIPTION)}</dc:description>
<meta property="dcterms:modified">{modified}</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="style.css" media-type="text/css"/>
{manifest}
</manifest>
<spine toc="ncx">
{spine}
</spine>
</package>
"""
    container = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""
    with zipfile.ZipFile(OUTPUT_FILE, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", STYLE, compress_type=zipfile.ZIP_DEFLATED)
        for _, href, _, content, _ in items:
            z.writestr(f"OEBPS/{href}", content, compress_type=zipfile.ZIP_DEFLATED)

    print()
    print(f"[OK] EPUB created: {OUTPUT_FILE}")
    print(f"[OK] File size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    print()
    print("To convert to MOBI/AZW3 for Kindle (requires Calibre):")
    print(f"  ebook-convert {OUTPUT_FILE} {OUTPUT_FILE.with_suffix('.azw3')}")

if __name__ == "__main__":
    import sys
    for key in select_books(sys.argv[1:]):
        configure(key)
        create_ebook()
        print()
