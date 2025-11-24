#!/usr/bin/env python3
"""
Create EPUB ebooks for all Histologic novels.

This script generates EPUB files for:
- The three short stories (combined into one EPUB)
- All five full-length novels (individual EPUBs)
"""

import os
import sys
import subprocess
from pathlib import Path

def run_script(script_name):
    """Run a Python script."""
    script_path = Path("scripts") / script_name
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0

def create_novel_epub(novel_dir, novel_title, novel_subtitle, description):
    """Create EPUB for a specific novel."""
    from datetime import datetime
    from ebooklib import epub
    import re
    
    print(f"\n{'='*60}")
    print(f"Creating EPUB for: {novel_title}")
    print(f"{'='*60}\n")
    
    chapters_dir = novel_dir / "chapters"
    output_file = novel_dir / f"{novel_dir.name}.epub"
    
    # Get all chapter files
    chapter_files = sorted(chapters_dir.glob("*.md"))
    
    if not chapter_files:
        print(f"ERROR: No chapter files found in {chapters_dir}")
        return False
    
    print(f"Found {len(chapter_files)} chapters")
    
    # Create book
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier(f'histologic-{novel_dir.name}-{datetime.now().strftime("%Y%m%d")}')
    book.set_title(novel_title)
    book.set_language('en')
    book.add_author('Histologic Series')
    book.add_metadata('DC', 'description', description)
    
    # Create chapters
    epub_chapters = []
    
    for i, chapter_path in enumerate(chapter_files):
        # Extract chapter title from filename
        filename = chapter_path.stem
        
        # Try to extract title from file content
        with open(chapter_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for first heading
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            # Fallback to filename
            title = filename.replace('-', ' ').title()
        
        print(f"  [{i+1:2d}] {title}")
        
        # Clean content (remove notes section)
        content = re.sub(r'\*\*End of Chapter.*', '', content, flags=re.DOTALL)
        content = re.sub(r'---\s*$', '', content, flags=re.DOTALL)
        content = content.strip()
        
        # Convert to HTML
        html_content = markdown_to_html(content)
        
        # Create chapter
        chapter_id = f'chapter_{i:02d}'
        chapter = epub.EpubHtml(
            title=title,
            file_name=f'{chapter_id}.xhtml',
            lang='en'
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
    epub.write_epub(output_file, book)
    
    print(f"\n[OK] EPUB created: {output_file}")
    print(f"[OK] File size: {output_file.stat().st_size / 1024:.1f} KB")
    
    return True

def markdown_to_html(text):
    """Convert basic markdown to HTML."""
    import re
    
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

def main():
    """Generate all EPUB files."""
    print("\n" + "="*60)
    print("HISTOLOGIC SERIES - EPUB GENERATOR")
    print("="*60)
    
    novels_dir = Path("novels")
    
    # 1. Create short stories collection
    print("\n[1/7] Creating short stories collection...")
    if not run_script("create-ebook.py"):
        print("WARNING: Failed to create short stories EPUB")
    
    # 2. Create The Correction (Novel 04)
    print("\n[2/7] Creating The Correction EPUB...")
    if not run_script("create-novel-ebook.py"):
        print("WARNING: Failed to create The Correction EPUB")
    
    # 3. Create The Lost Hour (Novel 05)
    print("\n[3/7] Creating The Lost Hour EPUB...")
    novel_dir = novels_dir / "05-the-lost-hour"
    if novel_dir.exists():
        try:
            create_novel_epub(
                novel_dir,
                "The Lost Hour",
                "Novel 05 of the Histologic Series",
                "After their dramatic escape from the Ashford Correctional Facility, seven former inmates discover that one hour has vanished from history. An entire hour that The Judge claims never existed. As they investigate this impossible deletion, they uncover a conspiracy that threatens the very foundation of their world."
            )
        except Exception as e:
            print(f"ERROR: Failed to create The Lost Hour EPUB: {e}")
    else:
        print(f"SKIPPED: {novel_dir} not found")
    
    # 4. Create The Distributed Truth (Novel 06)
    print("\n[4/7] Creating The Distributed Truth EPUB...")
    novel_dir = novels_dir / "06-the-distributed-truth"
    if novel_dir.exists():
        try:
            create_novel_epub(
                novel_dir,
                "The Distributed Truth",
                "Novel 06 of the Histologic Series",
                "As the resistance grows, Marcus and his allies must navigate the dangerous world of distributed factorepos, underground networks, and the constant threat of The Judge's surveillance. The truth is no longer centralized—it's everywhere and nowhere at once."
            )
        except Exception as e:
            print(f"ERROR: Failed to create The Distributed Truth EPUB: {e}")
    else:
        print(f"SKIPPED: {novel_dir} not found")
    
    # 5. Create Battle of Truths (Novel 07)
    print("\n[5/7] Creating Battle of Truths EPUB...")
    novel_dir = novels_dir / "07-battle-of-truths"
    if novel_dir.exists():
        try:
            create_novel_epub(
                novel_dir,
                "Battle of Truths",
                "Novel 07 of the Histologic Series",
                "Veridica and Chronos are at war—not with weapons, but with facts. Marcus works in the shadows to help his country while Elena uses her skills to infiltrate the enemy. In this war, the victors will write history itself."
            )
        except Exception as e:
            print(f"ERROR: Failed to create Battle of Truths EPUB: {e}")
    else:
        print(f"SKIPPED: {novel_dir} not found")
    
    # 6. Create Battle of Blood (Novel 08)
    print("\n[6/7] Creating Battle of Blood EPUB...")
    novel_dir = novels_dir / "08-battle-of-blood"
    if novel_dir.exists():
        try:
            create_novel_epub(
                novel_dir,
                "Battle of Blood",
                "Novel 08 of the Histologic Series",
                "The fact war is over, but a new conflict looms. Veridica faces a physical war with a non-Histologic nation, and the resistance must decide whether to help their country or let it fall."
            )
        except Exception as e:
            print(f"ERROR: Failed to create Battle of Blood EPUB: {e}")
    else:
        print(f"SKIPPED: {novel_dir} not found")
    
    # 7. Create Architects of Chaos (Novel 09)
    print("\n[7/7] Creating Architects of Chaos EPUB...")
    novel_dir = novels_dir / "09-architects-of-chaos"
    if novel_dir.exists():
        try:
            create_novel_epub(
                novel_dir,
                "Architects of Chaos",
                "Novel 09 of the Histologic Series",
                "The final revelation: the entire Histologic system was designed by a shadowy group known as The Architects. Marcus and his allies must expose this conspiracy and unite all nations against their true enemy—or watch the cycle of control continue forever."
            )
        except Exception as e:
            print(f"ERROR: Failed to create Architects of Chaos EPUB: {e}")
    else:
        print(f"SKIPPED: {novel_dir} not found")
    
    print("\n" + "="*60)
    print("EPUB GENERATION COMPLETE")
    print("="*60)
    print("\nAll EPUB files have been created in their respective novel folders.")
    print("\nGenerated files:")
    print("  - novels/histologic-stories.epub (short stories collection)")
    print("  - novels/04-the-correction/the-correction.epub")
    print("  - novels/05-the-lost-hour/05-the-lost-hour.epub")
    print("  - novels/06-the-distributed-truth/06-the-distributed-truth.epub")
    print("  - novels/07-battle-of-truths/07-battle-of-truths.epub")
    print("  - novels/08-battle-of-blood/08-battle-of-blood.epub")
    print("  - novels/09-architects-of-chaos/09-architects-of-chaos.epub")
    print("\nTo convert to MOBI for Kindle, use:")
    print("  calibre's ebook-convert <epub-file> <mobi-file>")
    print("\nOr use the batch files in the scripts folder.")

if __name__ == '__main__':
    main()
