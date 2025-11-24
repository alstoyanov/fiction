#!/usr/bin/env python3
"""
Export novel chapters to HTML with navigation.
"""

import os
import re
from pathlib import Path
import markdown

# Configuration
NOVEL_DIR = Path("novels/04-the-correction")
CHAPTERS_DIR = NOVEL_DIR / "chapters"
OUTPUT_DIR = NOVEL_DIR / "html-export"
TEMPLATE_FILE = Path("templates/novel-export-template.html")

# Novel metadata
NOVEL_TITLE = "The Correction"
NOVEL_SUBTITLE = "Novel 04 of the Histologic Series"

# Chapter order
CHAPTERS = [
    ("00-prologue.md", "Prologue", "The Conviction"),
    ("01-arrival.md", "Chapter 1", "Arrival"),
    ("02-the-sessions.md", "Chapter 2", "The Sessions"),
    ("03-the-enforcer.md", "Chapter 3", "The Enforcer"),
    ("04-the-outlaw.md", "Chapter 4", "The Outlaw"),
    ("05-the-technician.md", "Chapter 5", "The Technician"),
    ("06-the-doctor.md", "Chapter 6", "The Doctor"),
    ("07-the-journalist.md", "Chapter 7", "The Journalist"),
    ("08-the-pattern.md", "Chapter 8", "The Pattern"),
    ("09-the-evidence.md", "Chapter 9", "The Evidence"),
    ("10-the-triplets-reunite.md", "Chapter 10", "The Triplets Reunite"),
    ("11-the-network.md", "Chapter 11", "The Network"),
    ("12-the-corruption.md", "Chapter 12", "The Corruption"),
    ("13-the-conscience.md", "Chapter 13", "The Conscience"),
    ("14-the-story.md", "Chapter 14", "The Story"),
    ("15-the-believers-doubt.md", "Chapter 15", "The Believer's Doubt"),
    ("16-the-alliance.md", "Chapter 16", "The Alliance"),
    ("17-the-inside-help.md", "Chapter 17", "The Inside Help"),
    ("18-the-plan.md", "Chapter 18", "The Plan"),
    ("19-the-fact-storm.md", "Chapter 19", "The Fact Storm"),
    ("20-the-breakout.md", "Chapter 20", "The Breakout"),
    ("21-the-escape.md", "Chapter 21", "The Escape"),
    ("22-the-pursuit.md", "Chapter 22", "The Pursuit"),
    ("23-the-divergence.md", "Chapter 23", "The Divergence"),
    ("24-the-love.md", "Chapter 24", "The Love"),
    ("25-the-mission.md", "Chapter 25", "The Mission"),
    ("26-epilogue.md", "Epilogue", "Seven Paths"),
]

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
            --brass: #b8860b;
            --dark-brass: #8b6914;
            --light-brass: #daa520;
            --bg-dark: #1a1a1a;
            --bg-medium: #2a2a2a;
            --bg-light: #3a3a3a;
            --text-primary: #e0e0e0;
            --text-secondary: #b0b0b0;
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
            border-bottom: 3px solid var(--brass);
            margin-bottom: 3rem;
        }}

        .series-title {{
            font-size: 0.9rem;
            color: var(--brass);
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 0.5rem;
        }}

        h1 {{
            font-size: 3rem;
            color: var(--light-brass);
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}

        .novel-meta {{
            color: var(--text-secondary);
            font-style: italic;
            font-size: 1.1rem;
        }}

        .toc {{
            background: rgba(42, 42, 42, 0.6);
            border-left: 4px solid var(--brass);
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 4px;
        }}

        .toc h2 {{
            color: var(--brass);
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }}

        .part {{
            margin: 2rem 0;
        }}

        .part-title {{
            color: var(--light-brass);
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
            border-left: 3px solid var(--brass);
            transition: all 0.3s ease;
        }}

        .chapter-list a:hover {{
            background: var(--bg-medium);
            border-left-color: var(--light-brass);
            transform: translateX(5px);
        }}

        .chapter-number {{
            color: var(--brass);
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
            border-top: 2px solid var(--brass);
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
            
            <div class="part">
                <div class="part-title">Part One: The Gathering</div>
                <ul class="chapter-list">
                    <li><a href="00-prologue.html"><span class="chapter-number">Prologue:</span> The Conviction</a></li>
                    <li><a href="01-arrival.html"><span class="chapter-number">Chapter 1:</span> Arrival <span class="chapter-title">(Marcus)</span></a></li>
                    <li><a href="02-the-sessions.html"><span class="chapter-number">Chapter 2:</span> The Sessions <span class="chapter-title">(Kira)</span></a></li>
                    <li><a href="03-the-enforcer.html"><span class="chapter-number">Chapter 3:</span> The Enforcer <span class="chapter-title">(Dmitri)</span></a></li>
                    <li><a href="04-the-outlaw.html"><span class="chapter-number">Chapter 4:</span> The Outlaw <span class="chapter-title">(Alexei)</span></a></li>
                    <li><a href="05-the-technician.html"><span class="chapter-number">Chapter 5:</span> The Technician <span class="chapter-title">(Nikolai)</span></a></li>
                    <li><a href="06-the-doctor.html"><span class="chapter-number">Chapter 6:</span> The Doctor <span class="chapter-title">(Yuki)</span></a></li>
                    <li><a href="07-the-journalist.html"><span class="chapter-number">Chapter 7:</span> The Journalist <span class="chapter-title">(Isaiah)</span></a></li>
                </ul>
            </div>

            <div class="part">
                <div class="part-title">Part Two: The Cracks</div>
                <ul class="chapter-list">
                    <li><a href="08-the-pattern.html"><span class="chapter-number">Chapter 8:</span> The Pattern <span class="chapter-title">(Marcus)</span></a></li>
                    <li><a href="09-the-evidence.html"><span class="chapter-number">Chapter 9:</span> The Evidence <span class="chapter-title">(Kira)</span></a></li>
                    <li><a href="10-the-triplets-reunite.html"><span class="chapter-number">Chapter 10:</span> The Triplets Reunite <span class="chapter-title">(Dmitri)</span></a></li>
                    <li><a href="11-the-network.html"><span class="chapter-number">Chapter 11:</span> The Network <span class="chapter-title">(Alexei)</span></a></li>
                    <li><a href="12-the-corruption.html"><span class="chapter-number">Chapter 12:</span> The Corruption <span class="chapter-title">(Nikolai)</span></a></li>
                    <li><a href="13-the-conscience.html"><span class="chapter-number">Chapter 13:</span> The Conscience <span class="chapter-title">(Yuki)</span></a></li>
                    <li><a href="14-the-story.html"><span class="chapter-number">Chapter 14:</span> The Story <span class="chapter-title">(Isaiah)</span></a></li>
                </ul>
            </div>

            <div class="part">
                <div class="part-title">Part Three: The Plan</div>
                <ul class="chapter-list">
                    <li><a href="15-the-believers-doubt.html"><span class="chapter-number">Chapter 15:</span> The Believer's Doubt <span class="chapter-title">(Marcus)</span></a></li>
                    <li><a href="16-the-alliance.html"><span class="chapter-number">Chapter 16:</span> The Alliance <span class="chapter-title">(Kira)</span></a></li>
                    <li><a href="17-the-inside-help.html"><span class="chapter-number">Chapter 17:</span> The Inside Help <span class="chapter-title">(Dmitri)</span></a></li>
                    <li><a href="18-the-plan.html"><span class="chapter-number">Chapter 18:</span> The Plan <span class="chapter-title">(Alexei)</span></a></li>
                </ul>
            </div>

            <div class="part">
                <div class="part-title">Part Four: The Storm</div>
                <ul class="chapter-list">
                    <li><a href="19-the-fact-storm.html"><span class="chapter-number">Chapter 19:</span> The Fact Storm <span class="chapter-title">(Marcus)</span></a></li>
                    <li><a href="20-the-breakout.html"><span class="chapter-number">Chapter 20:</span> The Breakout <span class="chapter-title">(Kira)</span></a></li>
                    <li><a href="21-the-escape.html"><span class="chapter-number">Chapter 21:</span> The Escape <span class="chapter-title">(Dmitri)</span></a></li>
                    <li><a href="22-the-pursuit.html"><span class="chapter-number">Chapter 22:</span> The Pursuit <span class="chapter-title">(Alexei)</span></a></li>
                </ul>
            </div>

            <div class="part">
                <div class="part-title">Part Five: The Divergence</div>
                <ul class="chapter-list">
                    <li><a href="23-the-divergence.html"><span class="chapter-number">Chapter 23:</span> The Divergence <span class="chapter-title">(Isaiah)</span></a></li>
                    <li><a href="24-the-love.html"><span class="chapter-number">Chapter 24:</span> The Love <span class="chapter-title">(Kira)</span></a></li>
                    <li><a href="25-the-mission.html"><span class="chapter-number">Chapter 25:</span> The Mission <span class="chapter-title">(Marcus)</span></a></li>
                </ul>
            </div>

            <div class="part">
                <ul class="chapter-list">
                    <li><a href="26-epilogue.html"><span class="chapter-number">Epilogue:</span> Seven Paths</a></li>
                </ul>
            </div>
        </div>

        <footer>
            <p><strong>The Correction</strong> - Novel 04 of the Histologic Series</p>
            <p>© 2025 - All Rights Reserved</p>
            <p style="margin-top: 1rem; font-size: 0.8rem;">
                27 chapters | ~49,500 words | Complete novel
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




