#!/usr/bin/env python3
"""
Create EPUB ebook for "The Correction" novel.
"""

import os
import re
from pathlib import Path
from datetime import datetime, timezone
import html
import uuid
import zipfile

# Configuration
NOVEL_DIR = Path("novels/04-the-correction")
CHAPTERS_DIR = NOVEL_DIR / "chapters"
OUTPUT_FILE = NOVEL_DIR / "the-correction.epub"

# Novel metadata
NOVEL_TITLE = "The Correction"
NOVEL_SUBTITLE = "Novel 04 of the Histologic Series"
AUTHOR = "Histologic Series"
LANGUAGE = "en"
DESCRIPTION = """Marcus Chen believed in Veridica with his whole heart, and he did everything the system asked of him. It sent him to Ashford anyway, to a silent wing of glass cells where a programme called Continuity takes the belief out of people and leaves them empty.

Seven prisoners have been chosen: a believer, an architect of the factorepo, three brothers who cannot be broken, a doctor, and a journalist. To survive they must learn to look erased while staying themselves, find each other without speaking, and escape a building that can read their minds, before the day they are due to be finished."""

# Chapter order, grouped by part: (file, number, title, POV)
PARTS = [
    ('Prologue', [
        ('00-prologue.md', 'Prologue', 'The Conviction', 'Marcus'),
    ]),
    ('Part One: The Erasure', [
        ('01-cell-7h.md', 'Chapter 1', 'Cell 7-H', 'Marcus'),
        ('02-the-white-room.md', 'Chapter 2', 'The White Room', 'Marcus'),
        ('03-two-months.md', 'Chapter 3', 'Two Months', 'Marcus'),
        ('04-the-arrival.md', 'Chapter 4', 'The Arrival', 'Kira'),
        ('05-the-corrected.md', 'Chapter 5', 'The Corrected', 'Dmitri'),
        ('06-the-library.md', 'Chapter 6', 'The Library', 'Alexei'),
        ('07-the-observer.md', 'Chapter 7', 'The Observer', 'Tanaka'),
        ('08-the-pattern.md', 'Chapter 8', 'The Pattern', 'Isaiah'),
    ]),
    ('Part Two: The Connection', [
        ('09-the-recognition.md', 'Chapter 9', 'The Recognition', 'Marcus'),
        ('10-the-whisper.md', 'Chapter 10', 'The Whisper', 'Kira'),
        ('11-the-garden-meetings.md', 'Chapter 11', 'The Garden Meetings', 'Marcus'),
        ('12-the-discovery.md', 'Chapter 12', 'The Discovery', 'Nikolai'),
        ('13-the-revelation.md', 'Chapter 13', 'The Revelation', 'Dmitri'),
        ('14-the-message-system.md', 'Chapter 14', 'The Message System', 'Alexei'),
        ('15-the-triplet-story.md', 'Chapter 15', 'The Triplet Story', 'Nikolai'),
        ('16-the-conspiracy.md', 'Chapter 16', 'The Conspiracy', 'Marcus'),
        ('17-the-ally.md', 'Chapter 17', 'The Ally', 'Tanaka'),
    ]),
    ('Part Three: The Plan', [
        ('18-the-breaking-point.md', 'Chapter 18', 'The Breaking Point', 'Marcus'),
        ('19-the-alliance-forms.md', 'Chapter 19', 'The Alliance Forms', 'Kira'),
        ('20-the-impossible-plan.md', 'Chapter 20', 'The Impossible Plan', 'Dmitri'),
        ('21-the-single-node.md', 'Chapter 21', 'The Single Node', 'Nikolai'),
        ('22-the-sacrifice.md', 'Chapter 22', 'The Sacrifice', 'Isaiah'),
    ]),
    ('Part Four: The Storm', [
        ('23-the-fact-storm.md', 'Chapter 23', 'The Fact Storm', 'Marcus'),
        ('24-the-breakout.md', 'Chapter 24', 'The Breakout', 'Kira'),
        ('25-the-cost-of-freedom.md', 'Chapter 25', 'The Cost of Freedom', 'Dmitri'),
        ('26-the-pursuit.md', 'Chapter 26', 'The Pursuit', 'Alexei'),
    ]),
    ('Part Five: The Aftermath', [
        ('27-the-report.md', 'Chapter 27', 'The Report', 'Isaiah'),
        ('28-the-recovery.md', 'Chapter 28', 'The Recovery', 'Kira'),
        ('29-the-missions.md', 'Chapter 29', 'The Missions', 'Marcus'),
    ]),
    ('Epilogue', [
        ('30-epilogue.md', 'Epilogue', 'Seven Paths, One Truth', None),
    ]),
]
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
    create_ebook()
