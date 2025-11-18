# HTML Export Guide - Histologic Stories

## Quick Start

### Export All Stories (Windows)
Simply double-click:
```
scripts\export-all-stories.bat
```

### Export Single Story
```bash
python scripts\export-story-html.py novels\the-believers-fall
python scripts\export-story-html.py novels\the-stolen-fact
python scripts\export-story-html.py novels\the-divided-truth
```

## What Gets Created

Each story folder will contain an HTML file:
- `novels/the-believers-fall/the-believers-fall.html`
- `novels/the-stolen-fact/the-stolen-fact.html`
- `novels/the-divided-truth/the-divided-truth.html`

## Features

### Beautiful Design
- ✓ Professional typography with drop caps
- ✓ Responsive layout (works on all devices)
- ✓ Dark mode support
- ✓ Reading progress indicator
- ✓ Smooth navigation

### Print-Ready
- ✓ Optimized for printing
- ✓ Proper page breaks
- ✓ Clean margins
- ✓ Professional formatting

### Story Information
- ✓ Word count and reading time
- ✓ Synopsis and themes
- ✓ Character information
- ✓ World-building elements
- ✓ Connections to other stories

## Viewing the HTML Files

### In Browser
1. Navigate to the story folder
2. Double-click the `.html` file
3. Opens in your default browser

### Printing
1. Open HTML file in browser
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Recommended settings:
   - Paper: A4 or Letter
   - Margins: Default
   - Background graphics: On
   - Scale: 100%

### Sharing
- Email the HTML file (self-contained, no external dependencies)
- Upload to web server
- Share via cloud storage

## Customization

### Template Location
```
templates/story-export-template.html
```

### Customize Colors
Edit the CSS variables in the template:
```css
:root {
    --primary-color: #1a1a2e;      /* Dark blue header */
    --accent-color: #0f3460;       /* Medium blue accents */
    --highlight-color: #e94560;    /* Red highlights */
}
```

### Customize Fonts
```css
:root {
    --font-serif: 'Georgia', 'Times New Roman', serif;
    --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', ...;
}
```

## Technical Details

### Requirements
- Python 3.6 or higher
- No external dependencies

### How It Works
1. Reads `story.md` (markdown)
2. Reads `README.md` (metadata)
3. Converts markdown to HTML
4. Applies beautiful template
5. Saves HTML file

### File Structure
```
histologic/
├── scripts/
│   ├── export-story-html.py          # Export script
│   ├── export-all-stories.bat        # Batch file (Windows)
│   └── README-EXPORT.md              # Detailed docs
├── templates/
│   └── story-export-template.html    # HTML template
└── novels/
    ├── the-believers-fall/
    │   ├── story.md
    │   ├── README.md
    │   └── the-believers-fall.html   # ← Generated
    ├── the-stolen-fact/
    │   ├── story.md
    │   ├── README.md
    │   └── the-stolen-fact.html      # ← Generated
    └── the-divided-truth/
        ├── story.md
        ├── README.md
        └── the-divided-truth.html    # ← Generated
```

## Current Stories

### 1. The Believer's Fall
- **Word Count**: ~4,745 words
- **Reading Time**: ~24 minutes
- **Synopsis**: Marcus Chen, a true believer, falls in love with Elena, who turns out to be an outlaw recruiter. Despite remaining a believer, he's deemed compromised and sent to a correctional facility.

### 2. The Stolen Fact
- **Word Count**: ~4,445 words
- **Reading Time**: ~22 minutes
- **Synopsis**: Kira Osman, a meticulous fact recorder, discovers a fact she input has mysteriously vanished. Her investigation leads to her conviction as an outlaw and imprisonment in the same facility as Marcus.

### 3. The Divided Truth
- **Word Count**: ~7,918 words
- **Reading Time**: ~40 minutes
- **Synopsis**: Three men in the border zone—an enforcer, an outlaw, and a technician—are revealed to be identical triplets torn apart by their father's death. All three end up in a correctional facility, but their connection proves impossible to break.

## Browser Compatibility

The HTML works in:
- ✓ Chrome/Edge (latest)
- ✓ Firefox (latest)
- ✓ Safari (latest)
- ✓ Mobile browsers

## Troubleshooting

### "Python not found"
Install Python from python.org (version 3.6 or higher)

### "Script not found"
Make sure you're in the project root directory:
```bash
cd D:\Git\fiction\histologic
```

### "Story not found"
Check that the story folder contains `story.md`

### HTML looks wrong
Make sure you're opening the HTML file in a modern browser (Chrome, Firefox, Safari, Edge)

## Advanced Usage

### Custom Output Location
Modify the script to change output location:
```python
output_path = Path('exports') / f'{story_path.name}.html'
```

### Batch Processing
The batch file exports all stories at once. To add new stories, edit:
```
scripts\export-all-stories.bat
```

### Template Modifications
Create custom templates by copying and modifying:
```
templates\story-export-template.html
```

## Future Enhancements

Planned features:
- [ ] EPUB export
- [ ] PDF export
- [ ] Custom CSS themes
- [ ] Image embedding
- [ ] Footnotes support

## Support

For detailed documentation, see:
```
scripts/README-EXPORT.md
```

For template customization, see:
```
templates/story-export-template.html
```

---

**Last Updated**: November 18, 2025
**Version**: 1.0

**Quick Commands**:
- Export all: `scripts\export-all-stories.bat`
- Export one: `python scripts\export-story-html.py novels\[story-name]`
- View template: `templates\story-export-template.html`

