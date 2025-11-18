#!/usr/bin/env python3
"""
Export Histologic stories from Markdown to beautiful HTML pages.

Usage:
    python export-story-html.py <story-folder>
    
Example:
    python export-story-html.py novels/the-believers-fall
    python export-story-html.py novels/the-stolen-fact
    python export-story-html.py novels/the-divided-truth
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def markdown_to_html(markdown_text):
    """
    Convert markdown to HTML.
    Simple converter for story content.
    """
    html = markdown_text
    
    # Remove markdown metadata header (# Title at top)
    html = re.sub(r'^#\s+.*?\n', '', html, count=1)
    html = re.sub(r'^\*.*?\*\s*\n', '', html, count=1)
    
    # Convert headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 id="\1">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Convert horizontal rules (section breaks)
    html = re.sub(r'^---+$', '<hr>', html, flags=re.MULTILINE)
    
    # Convert emphasis
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Convert paragraphs
    paragraphs = html.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Skip if already HTML
        if para.startswith('<'):
            html_paragraphs.append(para)
        else:
            # Replace single newlines with spaces
            para = para.replace('\n', ' ')
            html_paragraphs.append(f'<p>{para}</p>')
    
    return '\n\n'.join(html_paragraphs)

def extract_story_info(readme_path):
    """Extract story information from README."""
    if not os.path.exists(readme_path):
        return {}
    
    readme = read_file(readme_path)
    info = {}
    
    # Extract title
    title_match = re.search(r'^#\s+(.+?)$', readme, re.MULTILINE)
    if title_match:
        info['title'] = title_match.group(1)
    
    # Extract synopsis
    synopsis_match = re.search(r'## Synopsis\s+(.+?)(?=\n##|\Z)', readme, re.DOTALL)
    if synopsis_match:
        info['description'] = synopsis_match.group(1).strip()
    
    # Extract themes
    themes = []
    themes_section = re.search(r'### Primary Themes\s+(.+?)(?=\n###|\n##|\Z)', readme, re.DOTALL)
    if themes_section:
        theme_matches = re.findall(r'^\*\*(.+?)\*\*:', themes_section.group(1), re.MULTILINE)
        themes.extend(theme_matches)
    
    info['themes'] = themes
    
    # Extract characters
    characters = []
    chars_section = re.search(r'## Characters\s+(.+?)(?=\n##|\Z)', readme, re.DOTALL)
    if chars_section:
        char_matches = re.findall(r'###\s+(.+?)\s+-\s+(.+?)$', chars_section.group(1), re.MULTILINE)
        characters = [f"{name} - {desc}" for name, desc in char_matches]
    
    info['characters'] = characters
    
    # Extract world-building
    worldbuilding = []
    wb_section = re.search(r'## World-Building Introduced\s+(.+?)(?=\n##|\Z)', readme, re.DOTALL)
    if wb_section:
        wb_matches = re.findall(r'###\s+(.+?)$', wb_section.group(1), re.MULTILINE)
        worldbuilding.extend(wb_matches)
    
    info['worldbuilding'] = worldbuilding
    
    # Extract connections
    connections = []
    conn_section = re.search(r'## Connections to Other Stories\s+(.+?)(?=\n##|\Z)', readme, re.DOTALL)
    if conn_section:
        info['connections'] = conn_section.group(1).strip()
    
    return info

def count_words(text):
    """Count words in text."""
    # Remove HTML tags for counting
    text = re.sub(r'<[^>]+>', '', text)
    words = text.split()
    return len(words)

def estimate_reading_time(word_count):
    """Estimate reading time (assuming 200 words per minute)."""
    return max(1, round(word_count / 200))

def create_html_export(story_folder):
    """Create HTML export for a story."""
    story_path = Path(story_folder)
    
    if not story_path.exists():
        print(f"Error: Story folder '{story_folder}' not found.")
        return
    
    # Read story markdown
    story_md_path = story_path / 'story.md'
    if not story_md_path.exists():
        print(f"Error: story.md not found in '{story_folder}'.")
        return
    
    print(f"Processing {story_folder}...")
    
    story_md = read_file(story_md_path)
    
    # Extract title from markdown
    title_match = re.search(r'^#\s+(.+?)$', story_md, re.MULTILINE)
    title = title_match.group(1) if title_match else story_path.name.replace('-', ' ').title()
    
    # Extract subtitle
    subtitle_match = re.search(r'^\*(.+?)\*$', story_md, re.MULTILINE)
    subtitle = subtitle_match.group(1) if subtitle_match else "A Short Story in the Histologic Universe"
    
    # Read README for metadata
    readme_path = story_path / 'README.md'
    story_info = extract_story_info(readme_path)
    
    # Use extracted info or defaults
    description = story_info.get('description', 'A story set in the Histologic universe.')
    themes = story_info.get('themes', [])
    characters = story_info.get('characters', [])
    worldbuilding = story_info.get('worldbuilding', [])
    connections = story_info.get('connections', 'Part of the Histologic universe.')
    
    # Convert markdown to HTML
    story_html = markdown_to_html(story_md)
    
    # Calculate stats
    word_count = count_words(story_html)
    reading_time = estimate_reading_time(word_count)
    
    # Read template
    template_path = Path(__file__).parent.parent / 'templates' / 'story-export-template.html'
    template = read_file(template_path)
    
    # Format themes list
    themes_html = '\n'.join([f'<li><strong>{theme}</strong></li>' for theme in themes])
    if not themes_html:
        themes_html = '<li>Truth vs. Freedom</li><li>Order vs. Chaos</li>'
    
    # Format characters list
    characters_html = '\n'.join([f'<li>{char}</li>' for char in characters])
    if not characters_html:
        characters_html = '<li>Various characters in the Histologic universe</li>'
    
    # Format worldbuilding
    worldbuilding_html = ', '.join(worldbuilding) if worldbuilding else 'Histologic system, factorepo, The Judge'
    
    # Replace placeholders
    html = template.replace('{{STORY_TITLE}}', title)
    html = html.replace('{{STORY_SUBTITLE}}', subtitle)
    html = html.replace('{{STORY_DESCRIPTION}}', description)
    html = html.replace('{{STORY_CONTENT}}', story_html)
    html = html.replace('{{WORD_COUNT}}', f'{word_count:,}')
    html = html.replace('{{READING_TIME}}', str(reading_time))
    html = html.replace('{{PUBLICATION_DATE}}', datetime.now().strftime('%B %d, %Y'))
    html = html.replace('{{YEAR}}', str(datetime.now().year))
    html = html.replace('{{THEMES_LIST}}', themes_html)
    html = html.replace('{{CHARACTERS_LIST}}', characters_html)
    html = html.replace('{{WORLDBUILDING_ELEMENTS}}', worldbuilding_html)
    html = html.replace('{{STORY_CONNECTIONS}}', connections)
    
    # Write output
    output_path = story_path / f'{story_path.name}.html'
    write_file(output_path, html)
    
    print(f"[OK] Created: {output_path}")
    print(f"  - {word_count:,} words")
    print(f"  - ~{reading_time} minute read")
    print(f"  - {len(themes)} themes")
    print(f"  - {len(characters)} characters")

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python export-story-html.py <story-folder>")
        print("\nAvailable stories:")
        novels_path = Path(__file__).parent.parent / 'novels'
        if novels_path.exists():
            for folder in sorted(novels_path.iterdir()):
                if folder.is_dir() and (folder / 'story.md').exists():
                    print(f"  - {folder}")
        sys.exit(1)
    
    story_folder = sys.argv[1]
    
    # If relative path, make it absolute
    if not os.path.isabs(story_folder):
        base_path = Path(__file__).parent.parent
        story_folder = base_path / story_folder
    
    create_html_export(story_folder)
    print("\n[OK] Export complete!")

if __name__ == '__main__':
    main()

