#!/usr/bin/env python3
"""
Export novel chapters to HTML with navigation.
"""

import os
import re
from pathlib import Path
try:
    import markdown
except ImportError:  # fall back to a minimal converter for the chapter markdown subset
    import html as _html

    class markdown:  # noqa: N801 - mimics the markdown module's API
        @staticmethod
        def markdown(text, extensions=None):
            def inline(t):
                t = _html.escape(t, quote=False)
                t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
                return re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
            out = []
            for block in re.split(r'\n\s*\n', text):
                block = block.strip()
                if not block:
                    continue
                if block == '---':
                    out.append('<hr>')
                elif block.startswith('## '):
                    out.append(f'<h2>{inline(block[3:])}</h2>')
                elif block.startswith('# '):
                    out.append(f'<h1>{inline(block[2:])}</h1>')
                else:
                    out.append(f'<p>{inline(" ".join(block.splitlines()))}</p>')
            return "\n".join(out)

# Configuration
NOVEL_DIR = Path("novels/04-the-correction")
CHAPTERS_DIR = NOVEL_DIR / "chapters"
OUTPUT_DIR = NOVEL_DIR / "html-export"
TEMPLATE_FILE = Path("templates/novel-export-template.html")

# Novel metadata
NOVEL_TITLE = "The Correction"
NOVEL_SUBTITLE = "Novel 04 of the Histologic Series"

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
CHAPTERS = [(f, n, t) for _, chs in PARTS for (f, n, t, _pov) in chs]

def extract_chapter_info(content):
    """Extract POV, timeline, and word count from chapter notes."""
    info = {}
    
    # Look for Notes section
    notes_match = re.search(r'## Notes\s+(.*?)(?=##|$)', content, re.DOTALL)
    if notes_match:
        notes = notes_match.group(1)
        
        # Extract POV
        pov_match = re.search(r'\*\*POV\*\*:\s*(.+?)(?:\n|$)', notes)
        if pov_match:
            info['pov'] = pov_match.group(1).strip()
        
        # Extract Timeline
        timeline_match = re.search(r'\*\*Timeline\*\*:\s*(.+?)(?:\n|$)', notes)
        if timeline_match:
            info['timeline'] = timeline_match.group(1).strip()
        
        # Extract Word Count
        word_match = re.search(r'\*Word Count:\s*~?([0-9,]+)', notes)
        if word_match:
            info['word_count'] = word_match.group(1).strip()
    
    return info

def clean_content(content):
    """Remove the Notes section and everything after 'End of Chapter'."""
    # Remove everything from "End of Chapter" onwards
    content = re.sub(r'\*\*End of Chapter.*', '', content, flags=re.DOTALL)
    
    # Remove the horizontal rule before notes if present
    content = re.sub(r'---\s*$', '', content, flags=re.DOTALL)
    
    return content.strip()

def convert_chapter(chapter_file, chapter_num, chapter_title, prev_chapter, next_chapter):
    """Convert a single chapter to HTML."""
    
    # Read chapter content
    chapter_path = CHAPTERS_DIR / chapter_file
    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract info before cleaning
    chapter_info = extract_chapter_info(content)
    
    # Clean content
    content = clean_content(content)
    
    # Convert markdown to HTML
    html_content = markdown.markdown(content, extensions=['extra', 'nl2br'])
    
    # Read template
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Build chapter info box
    info_parts = []
    if chapter_info.get('pov'):
        info_parts.append(f"<strong>POV:</strong> {chapter_info['pov']}")
    if chapter_info.get('timeline'):
        info_parts.append(f"<strong>Timeline:</strong> {chapter_info['timeline']}")
    if chapter_info.get('word_count'):
        info_parts.append(f"<strong>Word Count:</strong> ~{chapter_info['word_count']} words")
    
    if info_parts:
        chapter_info_html = f'<div class="chapter-info">{" | ".join(info_parts)}</div>'
    else:
        chapter_info_html = ''
    
    # Build navigation buttons
    if prev_chapter:
        prev_filename = prev_chapter[0].replace('.md', '.html')
        prev_title = f"{prev_chapter[1]}: {prev_chapter[2]}"
        prev_button = f'<a href="{prev_filename}" class="nav-button">← Previous: {prev_title}</a>'
    else:
        prev_button = '<span class="nav-button disabled">← Previous</span>'
    
    if next_chapter:
        next_filename = next_chapter[0].replace('.md', '.html')
        next_title = f"{next_chapter[1]}: {next_chapter[2]}"
        next_button = f'<a href="{next_filename}" class="nav-button">Next: {next_title} →</a>'
    else:
        next_button = '<span class="nav-button disabled">Next →</span>'
    
    # Current chapter indicator
    current_chapter = f"{chapter_num}: {chapter_title}"
    
    # Replace template variables
    html = template.replace('{{TITLE}}', NOVEL_TITLE)
    html = html.replace('{{SUBTITLE}}', NOVEL_SUBTITLE)
    html = html.replace('{{CONTENT}}', html_content)
    html = html.replace('{{CHAPTER_INFO}}', chapter_info_html)
    html = html.replace('{{PREV_BUTTON}}', prev_button)
    html = html.replace('{{NEXT_BUTTON}}', next_button)
    html = html.replace('{{CURRENT_CHAPTER}}', current_chapter)
    
    # Write output
    output_filename = chapter_file.replace('.md', '.html')
    output_path = OUTPUT_DIR / output_filename
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return output_filename

def create_index():
    """Create an index page with all chapters."""
    toc_parts = []
    for part_title, chapters in PARTS:
        items = []
        for f, num, title, pov in chapters:
            pov_html = f' <span class="chapter-title">({pov})</span>' if pov else ''
            items.append(f'                    <li><a href="{f.replace(".md", ".html")}"><span class="chapter-number">{num}:</span> {title}{pov_html}</a></li>')
        toc_parts.append('            <div class="part">\n'
                         f'                <div class="part-title">{part_title}</div>\n'
                         '                <ul class="chapter-list">\n' + '\n'.join(items) + '\n'
                         '                </ul>\n            </div>')
    toc_html = '\n\n'.join(toc_parts)
    total_words = sum(len((CHAPTERS_DIR / f).read_text(encoding='utf-8').split()) for f, _, _ in CHAPTERS)
    
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{NOVEL_TITLE} - Table of Contents</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --line: #3d7ea6;
            --line-dark: #2b5d7d;
            --heading: #1f4e6b;
            --bg-dark: #f4f6f8;
            --bg-medium: #ffffff;
            --bg-light: #e9edf1;
            --text-primary: #1c2530;
            --text-secondary: #5b6775;
        }}

        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.8;
            color: var(--text-primary);
            background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-medium) 100%);
            min-height: 100vh;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}

        header {{
            text-align: center;
            padding: 3rem 0;
            border-bottom: 3px solid var(--line);
            margin-bottom: 3rem;
        }}

        .series-title {{
            font-size: 0.9rem;
            color: var(--line);
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 0.5rem;
        }}

        h1 {{
            font-size: 3rem;
            color: var(--heading);
            margin-bottom: 1rem;
            text-shadow: none;
        }}

        .novel-meta {{
            color: var(--text-secondary);
            font-style: italic;
            font-size: 1.1rem;
        }}

        .toc {{
            background: rgba(233, 237, 241, 0.8);
            border-left: 4px solid var(--line);
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 4px;
        }}

        .toc h2 {{
            color: var(--line);
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }}

        .part {{
            margin: 2rem 0;
        }}

        .part-title {{
            color: var(--heading);
            font-size: 1.3rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        .chapter-list {{
            list-style: none;
        }}

        .chapter-list li {{
            margin: 0.75rem 0;
        }}

        .chapter-list a {{
            color: var(--text-primary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            display: block;
            background: var(--bg-light);
            border-left: 3px solid var(--line);
            transition: all 0.3s ease;
        }}

        .chapter-list a:hover {{
            background: var(--bg-medium);
            border-left-color: var(--heading);
            transform: translateX(5px);
        }}

        .chapter-number {{
            color: var(--line);
            font-weight: bold;
            margin-right: 0.5rem;
        }}

        .chapter-title {{
            color: var(--text-secondary);
            font-style: italic;
            margin-left: 0.5rem;
        }}

        footer {{
            text-align: center;
            padding: 3rem 0;
            margin-top: 4rem;
            border-top: 2px solid var(--line);
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="series-title">Histologic Series</div>
            <h1>{NOVEL_TITLE}</h1>
            <div class="novel-meta">{NOVEL_SUBTITLE}</div>
        </header>

        <div class="toc">
            <h2>Table of Contents</h2>
{toc_html}
        </div>

        <footer>
            <p><strong>The Correction</strong> - Novel 04 of the Histologic Series</p>
            <p>© 2026 - All Rights Reserved</p>
            <p style="margin-top: 1rem; font-size: 0.8rem;">
                Prologue, 29 chapters and Epilogue | ~{total_words:,} words
            </p>
        </footer>
    </div>
</body>
</html>
"""
    
    index_path = OUTPUT_DIR / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    return "index.html"

def main():
    """Main export function."""
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Exporting novel chapters to HTML...")
    print(f"Novel: {NOVEL_TITLE}")
    print(f"Chapters: {len(CHAPTERS)}")
    print()
    
    # Convert each chapter
    for i, (filename, chapter_num, chapter_title) in enumerate(CHAPTERS):
        prev_chapter = CHAPTERS[i-1] if i > 0 else None
        next_chapter = CHAPTERS[i+1] if i < len(CHAPTERS)-1 else None
        
        output_file = convert_chapter(filename, chapter_num, chapter_title, prev_chapter, next_chapter)
        print(f"[OK] Created: {output_file}")
    
    # Create index
    index_file = create_index()
    print(f"[OK] Created: {index_file}")
    
    print()
    print("[OK] Export complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Open {OUTPUT_DIR}/index.html to start reading")

if __name__ == "__main__":
    main()




