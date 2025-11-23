#!/usr/bin/env python3
"""
Create an EPUB ebook from Histologic stories.

This script bundles multiple stories into a single EPUB file that can be:
- Read directly on most e-readers
- Converted to MOBI for Kindle using Calibre
- Uploaded to Amazon KDP

Usage:
    python create-ebook.py
    
Output:
    histologic-stories.epub (in the project root)
"""

import os
import zipfile
import uuid
from pathlib import Path
from datetime import datetime

def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def markdown_to_html_simple(text):
    """Convert markdown to simple HTML for EPUB."""
    import re
    
    # Remove markdown header
    text = re.sub(r'^#\s+.*?\n', '', text, count=1)
    text = re.sub(r'^\*.*?\*\s*\n', '', text, count=1)
    
    # Convert headers
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Convert horizontal rules
    text = re.sub(r'^---+$', '<hr class="scene-break"/>', text, flags=re.MULTILINE)
    
    # Convert emphasis
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Convert paragraphs
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if para.startswith('<'):
            html_paragraphs.append(para)
        else:
            para = para.replace('\n', ' ')
            html_paragraphs.append(f'<p>{para}</p>')
    
    return '\n'.join(html_paragraphs)

def create_epub():
    """Create EPUB file."""
    print("Creating Histologic Stories EPUB...")
    
    # Create temp directory for EPUB contents
    epub_dir = Path('temp_epub')
    epub_dir.mkdir(exist_ok=True)
    
    # EPUB structure
    meta_inf = epub_dir / 'META-INF'
    meta_inf.mkdir(exist_ok=True)
    
    oebps = epub_dir / 'OEBPS'
    oebps.mkdir(exist_ok=True)
    
    # Generate UUID for this book
    book_uuid = str(uuid.uuid4())
    
    # 1. Create mimetype file
    write_file(epub_dir / 'mimetype', 'application/epub+zip')
    
    # 2. Create container.xml
    container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
    write_file(meta_inf / 'container.xml', container_xml)
    
    # 3. Create CSS
    css = '''
body {
    font-family: Georgia, serif;
    line-height: 1.6;
    margin: 1em;
}

h1, h2, h3 {
    font-family: sans-serif;
    page-break-after: avoid;
}

h1 {
    font-size: 2em;
    margin-top: 1em;
    margin-bottom: 0.5em;
    text-align: center;
}

h2 {
    font-size: 1.5em;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

h3 {
    font-size: 1.2em;
    margin-top: 1em;
    margin-bottom: 0.5em;
}

p {
    margin: 0 0 1em 0;
    text-align: justify;
    text-indent: 1.5em;
}

p.first {
    text-indent: 0;
}

.scene-break {
    border: none;
    text-align: center;
    margin: 2em 0;
}

.scene-break::before {
    content: "* * *";
    font-size: 1.2em;
}

.story-title {
    font-size: 2.5em;
    text-align: center;
    margin: 2em 0 1em 0;
    page-break-before: always;
}

.story-subtitle {
    font-style: italic;
    text-align: center;
    margin-bottom: 3em;
}

.copyright {
    font-size: 0.9em;
    text-align: center;
    margin: 2em 0;
}
'''
    write_file(oebps / 'stylesheet.css', css)
    
    # 4. Create title page
    title_page = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Histologic Stories</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
    <div style="text-align: center; margin-top: 30%;">
        <h1 style="font-size: 3em; margin-bottom: 0.2em;">HISTOLOGIC</h1>
        <h2 style="font-weight: normal; margin-top: 0;">Stories from a Future Where History is Science</h2>
        <p style="margin-top: 3em; font-style: italic;">Three Short Stories</p>
    </div>
</body>
</html>'''
    write_file(oebps / 'title.xhtml', title_page)
    
    # 5. Create copyright page
    copyright_page = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Copyright</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
    <div class="copyright">
        <h2>Copyright</h2>
        <p>© {datetime.now().year} Histologic Universe. All rights reserved.</p>
        <p>This is a work of fiction. Names, characters, places, and incidents are products of the author's imagination or are used fictitiously.</p>
        <p style="margin-top: 2em;">Published: {datetime.now().strftime('%B %Y')}</p>
        <p>Version 1.0</p>
    </div>
</body>
</html>'''
    write_file(oebps / 'copyright.xhtml', copyright_page)
    
    # 6. Create table of contents page
    toc_page = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Contents</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
    <h1>Contents</h1>
    <nav epub:type="toc">
        <ol style="list-style-type: none;">
            <li><a href="story1.xhtml">The Believer's Fall</a></li>
            <li><a href="story2.xhtml">The Stolen Fact</a></li>
            <li><a href="story3.xhtml">The Divided Truth</a></li>
            <li><a href="about.xhtml">About the Histologic Universe</a></li>
        </ol>
    </nav>
</body>
</html>'''
    write_file(oebps / 'toc.xhtml', toc_page)
    
    # 7. Convert stories
    stories = [
        {
            'folder': 'novels/the-believers-fall',
            'title': 'The Believer\'s Fall',
            'subtitle': 'A Short Story in the Histologic Universe',
            'filename': 'story1.xhtml'
        },
        {
            'folder': 'novels/the-stolen-fact',
            'title': 'The Stolen Fact',
            'subtitle': 'A Short Story in the Histologic Universe',
            'filename': 'story2.xhtml'
        },
        {
            'folder': 'novels/the-divided-truth',
            'title': 'The Divided Truth',
            'subtitle': 'A Short Story in the Histologic Universe',
            'filename': 'story3.xhtml'
        }
    ]
    
    manifest_items = []
    spine_items = []
    
    for i, story in enumerate(stories, 1):
        story_path = Path(story['folder']) / 'story.md'
        if not story_path.exists():
            print(f"Warning: {story_path} not found, skipping...")
            continue
        
        print(f"Processing: {story['title']}...")
        
        story_md = read_file(story_path)
        story_html = markdown_to_html_simple(story_md)
        
        xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>{story['title']}</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
    <h1 class="story-title">{story['title']}</h1>
    <p class="story-subtitle">{story['subtitle']}</p>
    {story_html}
</body>
</html>'''
        
        write_file(oebps / story['filename'], xhtml)
        manifest_items.append(f'    <item id="story{i}" href="{story["filename"]}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'    <itemref idref="story{i}"/>')
    
    # 8. Create about page
    about_page = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>About the Histologic Universe</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
    <h1>About the Histologic Universe</h1>
    
    <h2>The World</h2>
    <p>The Histologic universe is set on a futuristic Earth where history has become an exact science. Through advanced computing, universal language, and rigorous logical verification, historical facts are stored in massive databases called factorepos and used as the foundation for all truth, law, and governance.</p>
    
    <p>In this world, nations are no longer defined by language, ethnicity, or geography, but by which version of history they believe. These histonations exist in a state of perpetual tension, as each possesses its own "truth" that may contradict the truths of others.</p>
    
    <h2>Key Concepts</h2>
    <p><strong>Factorepo:</strong> A massive database storing all historical facts with precise time, location, and involved parties. Every fact is verified against all others for logical consistency.</p>
    
    <p><strong>The Judge:</strong> A supercomputer that resolves all legal disputes by analyzing the factorepo through logical deduction. Its decisions are absolute and cannot be appealed.</p>
    
    <p><strong>Outlaws:</strong> People who doubt their histonation's truth. They must choose between corrective facilities (forced belief) or exile.</p>
    
    <p><strong>Fact Wars:</strong> Conflicts between histonations fought through factorepo contradictions rather than physical weapons, though the psychological casualties are real.</p>
    
    <h2>The Stories</h2>
    <p><strong>The Believer's Fall</strong> introduces Marcus Chen, a true believer who falls in love with an outlaw recruiter and finds himself condemned despite his faith.</p>
    
    <p><strong>The Stolen Fact</strong> follows Kira Osman, who discovers a fact she recorded has mysteriously vanished, leading to her conviction as an outlaw.</p>
    
    <p><strong>The Divided Truth</strong> tells the story of three identical triplets torn apart by ideology—an enforcer, an outlaw, and a mediator—all ending up in the same correctional facility.</p>
    
    <h2>Themes</h2>
    <p>The Histologic universe explores fundamental questions about truth, freedom, certainty, and the cost of absolute knowledge. What happens when history becomes law? When doubt becomes crime? When the past controls the future?</p>
</body>
</html>'''
    write_file(oebps / 'about.xhtml', about_page)
    
    # 9. Create content.opf (package document)
    content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookID">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:title>Histologic Stories: Three Tales from a Future Where History is Science</dc:title>
        <dc:creator>Histologic Universe</dc:creator>
        <dc:language>en</dc:language>
        <dc:identifier id="BookID">urn:uuid:{book_uuid}</dc:identifier>
        <dc:publisher>Histologic Universe</dc:publisher>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:description>Three interconnected short stories set in a future where history has become an exact science. Follow characters as they navigate a world where truth is absolute, doubt is crime, and the past controls the future.</dc:description>
        <dc:subject>Science Fiction</dc:subject>
        <dc:subject>Dystopia</dc:subject>
        <dc:subject>Philosophy</dc:subject>
        <meta property="dcterms:modified">{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}Z</meta>
    </metadata>
    <manifest>
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="css" href="stylesheet.css" media-type="text/css"/>
        <item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>
        <item id="copyright" href="copyright.xhtml" media-type="application/xhtml+xml"/>
        <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml" properties="nav"/>
{chr(10).join(manifest_items)}
        <item id="about" href="about.xhtml" media-type="application/xhtml+xml"/>
    </manifest>
    <spine toc="ncx">
        <itemref idref="title"/>
        <itemref idref="copyright"/>
        <itemref idref="toc"/>
{chr(10).join(spine_items)}
        <itemref idref="about"/>
    </spine>
</package>'''
    write_file(oebps / 'content.opf', content_opf)
    
    # 10. Create toc.ncx (NCX navigation for older readers)
    toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="urn:uuid:{book_uuid}"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>Histologic Stories</text>
    </docTitle>
    <navMap>
        <navPoint id="title" playOrder="1">
            <navLabel><text>Title Page</text></navLabel>
            <content src="title.xhtml"/>
        </navPoint>
        <navPoint id="copyright" playOrder="2">
            <navLabel><text>Copyright</text></navLabel>
            <content src="copyright.xhtml"/>
        </navPoint>
        <navPoint id="toc" playOrder="3">
            <navLabel><text>Contents</text></navLabel>
            <content src="toc.xhtml"/>
        </navPoint>
        <navPoint id="story1" playOrder="4">
            <navLabel><text>The Believer's Fall</text></navLabel>
            <content src="story1.xhtml"/>
        </navPoint>
        <navPoint id="story2" playOrder="5">
            <navLabel><text>The Stolen Fact</text></navLabel>
            <content src="story2.xhtml"/>
        </navPoint>
        <navPoint id="story3" playOrder="6">
            <navLabel><text>The Divided Truth</text></navLabel>
            <content src="story3.xhtml"/>
        </navPoint>
        <navPoint id="about" playOrder="7">
            <navLabel><text>About the Histologic Universe</text></navLabel>
            <content src="about.xhtml"/>
        </navPoint>
    </navMap>
</ncx>'''
    write_file(oebps / 'toc.ncx', toc_ncx)
    
    # 11. Create EPUB file
    print("\nCreating EPUB file...")
    epub_path = Path('histologic-stories.epub')
    
    with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Add mimetype first (uncompressed)
        epub.write(epub_dir / 'mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
        
        # Add all other files
        for root, dirs, files in os.walk(epub_dir):
            for file in files:
                if file == 'mimetype':
                    continue
                file_path = Path(root) / file
                arcname = file_path.relative_to(epub_dir)
                epub.write(file_path, arcname)
    
    # Clean up temp directory
    import shutil
    shutil.rmtree(epub_dir)
    
    print(f"\n[OK] Created: {epub_path.absolute()}")
    print(f"     Size: {epub_path.stat().st_size / 1024:.1f} KB")
    print("\nNext steps:")
    print("  1. Open in Calibre to preview")
    print("  2. Convert to MOBI for Kindle: calibre-convert histologic-stories.epub histologic-stories.mobi")
    print("  3. Or use Amazon's Kindle Previewer to convert and test")

if __name__ == '__main__':
    create_epub()



