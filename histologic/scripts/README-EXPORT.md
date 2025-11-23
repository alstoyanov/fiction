# Story HTML Export System

This system converts Histologic stories from Markdown to beautiful, professional HTML pages suitable for reading, printing, or web publishing.

## Features

### Visual Design
- **Professional Layout**: Clean, readable design with proper typography
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Print-Friendly**: Optimized for printing with proper page breaks
- **Dark Mode**: Automatically adapts to system dark mode preference
- **Reading Progress**: Visual progress bar as you scroll
- **Smooth Navigation**: Table of contents with smooth scrolling

### Content Features
- **Story Metadata**: Word count, reading time, publication date
- **Story Information**: Synopsis, themes, characters, world-building
- **Proper Typography**: Drop caps, section breaks, proper spacing
- **Semantic HTML**: Clean, accessible markup

## Usage

### Export Single Story

```bash
python scripts/export-story-html.py novels/the-believers-fall
```

### Export All Stories (Windows)

```bash
scripts\export-all-stories.bat
```

### Export All Stories (Manual)

```bash
python scripts/export-story-html.py novels/the-believers-fall
python scripts/export-story-html.py novels/the-stolen-fact
python scripts/export-story-html.py novels/the-divided-truth
```

## Output

HTML files are created in each story folder:
- `novels/the-believers-fall/the-believers-fall.html`
- `novels/the-stolen-fact/the-stolen-fact.html`
- `novels/the-divided-truth/the-divided-truth.html`

## Template Customization

The HTML template is located at:
```
templates/story-export-template.html
```

### Customizable Elements

**Colors** (in `:root` CSS variables):
```css
--primary-color: #1a1a2e;      /* Dark blue */
--accent-color: #0f3460;       /* Medium blue */
--highlight-color: #e94560;    /* Red accent */
```

**Fonts**:
```css
--font-serif: 'Georgia', 'Times New Roman', serif;
--font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', ...;
```

**Layout**:
```css
--max-width: 800px;            /* Content width */
--spacing-unit: 1.5rem;        /* Base spacing */
```

### Template Placeholders

The template uses these placeholders (automatically replaced by the script):

- `{{STORY_TITLE}}` - Story title
- `{{STORY_SUBTITLE}}` - Story subtitle
- `{{STORY_DESCRIPTION}}` - Story synopsis
- `{{STORY_CONTENT}}` - Main story content (HTML)
- `{{WORD_COUNT}}` - Word count
- `{{READING_TIME}}` - Estimated reading time
- `{{PUBLICATION_DATE}}` - Export date
- `{{YEAR}}` - Current year
- `{{THEMES_LIST}}` - HTML list of themes
- `{{CHARACTERS_LIST}}` - HTML list of characters
- `{{WORLDBUILDING_ELEMENTS}}` - World-building elements
- `{{STORY_CONNECTIONS}}` - Connections to other stories

## File Structure

```
histologic/
├── scripts/
│   ├── export-story-html.py      # Python export script
│   ├── export-all-stories.bat    # Windows batch file
│   └── README-EXPORT.md          # This file
├── templates/
│   └── story-export-template.html # HTML template
└── novels/
    ├── the-believers-fall/
    │   ├── story.md
    │   ├── README.md
    │   └── the-believers-fall.html  # Generated
    ├── the-stolen-fact/
    │   ├── story.md
    │   ├── README.md
    │   └── the-stolen-fact.html     # Generated
    └── the-divided-truth/
        ├── story.md
        ├── README.md
        └── the-divided-truth.html   # Generated
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## How It Works

1. **Read Story**: Loads `story.md` from the story folder
2. **Read Metadata**: Extracts information from `README.md`
3. **Convert Markdown**: Converts markdown to HTML
4. **Calculate Stats**: Counts words, estimates reading time
5. **Apply Template**: Replaces placeholders in template
6. **Write Output**: Saves HTML file in story folder

## Markdown Support

The converter supports:

- **Headers**: `#`, `##`, `###`
- **Emphasis**: `*italic*`, `**bold**`, `***bold italic***`
- **Paragraphs**: Separated by blank lines
- **Section Breaks**: `---` becomes decorative separator
- **Drop Caps**: First letter of first paragraph is styled

## Browser Compatibility

The HTML output works in:
- ✓ Chrome/Edge (latest)
- ✓ Firefox (latest)
- ✓ Safari (latest)
- ✓ Mobile browsers (iOS Safari, Chrome Mobile)

## Print Settings

For best print results:
1. Open HTML file in browser
2. Print (Ctrl+P / Cmd+P)
3. Recommended settings:
   - Paper: A4 or Letter
   - Margins: Default
   - Background graphics: On (for header)
   - Scale: 100%

## Troubleshooting

### Script not found
Make sure you're running from the project root:
```bash
cd D:\Git\fiction\histologic
python scripts\export-story-html.py novels\the-believers-fall
```

### Template not found
Ensure `templates/story-export-template.html` exists in the project.

### Story not found
Check that the story folder contains `story.md`:
```bash
dir novels\the-believers-fall\story.md
```

### Python not found
Install Python 3.6+ from python.org

## Advanced Usage

### Custom Template
Create a copy of the template and modify:
```bash
copy templates\story-export-template.html templates\my-template.html
```

Then modify the script to use your template.

### Batch Processing
To export multiple stories programmatically:
```python
import os
from pathlib import Path

novels_path = Path('novels')
for story_folder in novels_path.iterdir():
    if story_folder.is_dir() and (story_folder / 'story.md').exists():
        os.system(f'python scripts/export-story-html.py {story_folder}')
```

## Future Enhancements

Potential improvements:
- [ ] EPUB export
- [ ] PDF export (via browser print or wkhtmltopdf)
- [ ] Custom CSS themes
- [ ] Table of contents generation
- [ ] Footnotes support
- [ ] Image embedding
- [ ] Multi-language support

## License

Part of the Histologic Universe project.

---

**Last Updated**: November 18, 2025
**Version**: 1.0



