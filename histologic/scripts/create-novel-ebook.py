#!/usr/bin/env python3
"""
Create EPUB ebook for "The Correction" novel.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from ebooklib import epub

# Configuration
NOVEL_DIR = Path("novels/04-the-correction")
CHAPTERS_DIR = NOVEL_DIR / "chapters"
OUTPUT_FILE = NOVEL_DIR / "the-correction.epub"

# Novel metadata
NOVEL_TITLE = "The Correction"
NOVEL_SUBTITLE = "Novel 04 of the Histologic Series"
AUTHOR = "Histologic Series"
LANGUAGE = "en"
DESCRIPTION = """On August 1, 2106, eight people were convicted of ideological contamination by The Judge—Veridica's supposedly infallible arbiter of truth. Their convictions were processed at exactly 14:37:22, simultaneously. But The Judge processes sequentially. This impossibility was the first crack in a system that claimed to be perfect.

This is the story of how eight inmates discovered that crack, exposed systematic corruption, escaped together, and began a revolution that would change their world forever."""

# Chapter order
CHAPTERS = [
    ("00-prologue.md", "Prologue: The Conviction"),
    ("01-arrival.md", "Chapter 1: Arrival"),
    ("02-the-sessions.md", "Chapter 2: The Sessions"),
    ("03-the-enforcer.md", "Chapter 3: The Enforcer"),
    ("04-the-outlaw.md", "Chapter 4: The Outlaw"),
    ("05-the-technician.md", "Chapter 5: The Technician"),
    ("06-the-doctor.md", "Chapter 6: The Doctor"),
    ("07-the-journalist.md", "Chapter 7: The Journalist"),
    ("08-the-pattern.md", "Chapter 8: The Pattern"),
    ("09-the-evidence.md", "Chapter 9: The Evidence"),
    ("10-the-triplets-reunite.md", "Chapter 10: The Triplets Reunite"),
    ("11-the-network.md", "Chapter 11: The Network"),
    ("12-the-corruption.md", "Chapter 12: The Corruption"),
    ("13-the-conscience.md", "Chapter 13: The Conscience"),
    ("14-the-story.md", "Chapter 14: The Story"),
    ("15-the-believers-doubt.md", "Chapter 15: The Believer's Doubt"),
    ("16-the-alliance.md", "Chapter 16: The Alliance"),
    ("17-the-inside-help.md", "Chapter 17: The Inside Help"),
    ("18-the-plan.md", "Chapter 18: The Plan"),
    ("19-the-fact-storm.md", "Chapter 19: The Fact Storm"),
    ("20-the-breakout.md", "Chapter 20: The Breakout"),
    ("21-the-escape.md", "Chapter 21: The Escape"),
    ("22-the-pursuit.md", "Chapter 22: The Pursuit"),
    ("23-the-divergence.md", "Chapter 23: The Divergence"),
    ("24-the-love.md", "Chapter 24: The Love"),
    ("25-the-mission.md", "Chapter 25: The Mission"),
    ("26-epilogue.md", "Epilogue: Seven Paths"),
]

def clean_content(content):
    """Remove the Notes section and everything after 'End of Chapter'."""
    # Remove everything from "End of Chapter" onwards
    content = re.sub(r'\*\*End of Chapter.*', '', content, flags=re.DOTALL)
    
    # Remove the horizontal rule before notes if present
    content = re.sub(r'---\s*$', '', content, flags=re.DOTALL)
    
    return content.strip()

def markdown_to_html(text):
    """Convert basic markdown to HTML."""
    # Headers
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Emphasis
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Horizontal rules
    text = re.sub(r'^---$', r'<hr/>', text, flags=re.MULTILINE)
    
    # Paragraphs
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            para = f'<p>{para}</p>'
        html_paragraphs.append(para)
    
    return '\n\n'.join(html_paragraphs)

def create_ebook():
    """Create the EPUB ebook."""
    
    print(f"Creating EPUB ebook for: {NOVEL_TITLE}")
    print(f"Chapters: {len(CHAPTERS)}")
    print()
    
    # Create book
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier(f'histologic-04-the-correction-{datetime.now().strftime("%Y%m%d")}')
    book.set_title(NOVEL_TITLE)
    book.set_language(LANGUAGE)
    book.add_author(AUTHOR)
    book.add_metadata('DC', 'description', DESCRIPTION)
    
    # Create chapters
    epub_chapters = []
    
    for i, (filename, title) in enumerate(CHAPTERS):
        print(f"Processing: {title}")
        
        # Read chapter content
        chapter_path = CHAPTERS_DIR / filename
        with open(chapter_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean content
        content = clean_content(content)
        
        # Convert to HTML
        html_content = markdown_to_html(content)
        
        # Create chapter
        chapter_id = f'chapter_{i:02d}'
        chapter = epub.EpubHtml(
            title=title,
            file_name=f'{chapter_id}.xhtml',
            lang=LANGUAGE
        )
        
        chapter.content = f'''
        <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{title}</h1>
            {html_content}
        </body>
        </html>
        '''
        
        book.add_item(chapter)
        epub_chapters.append(chapter)
    
    # Add CSS
    style = '''
    @namespace epub "http://www.idpf.org/2007/ops";
    
    body {
        font-family: Georgia, serif;
        line-height: 1.8;
        margin: 2em;
    }
    
    h1 {
        font-size: 2em;
        margin-top: 1em;
        margin-bottom: 0.5em;
        text-align: center;
        page-break-before: always;
    }
    
    h2 {
        font-size: 1.5em;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }
    
    h3 {
        font-size: 1.2em;
        margin-top: 0.8em;
        margin-bottom: 0.4em;
    }
    
    p {
        text-align: justify;
        margin-bottom: 1em;
        text-indent: 1.5em;
    }
    
    p:first-of-type {
        text-indent: 0;
    }
    
    em {
        font-style: italic;
    }
    
    strong {
        font-weight: bold;
    }
    
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 2em 0;
    }
    '''
    
    css = epub.EpubItem(
        uid="style",
        file_name="style.css",
        media_type="text/css",
        content=style
    )
    book.add_item(css)
    
    # Add default NCX and Nav files
    book.toc = tuple(epub_chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Define spine
    book.spine = ['nav'] + epub_chapters
    
    # Write EPUB file
    epub.write_epub(OUTPUT_FILE, book)
    
    print()
    print(f"[OK] EPUB created: {OUTPUT_FILE}")
    print(f"[OK] File size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    print()
    print("To convert to MOBI for Kindle:")
    print(f"  calibre's ebook-convert {OUTPUT_FILE} {OUTPUT_FILE.with_suffix('.mobi')}")
    print()
    print("Or use the batch file:")
    print("  scripts\\convert-novel-to-kindle.bat")

if __name__ == "__main__":
    create_ebook()

