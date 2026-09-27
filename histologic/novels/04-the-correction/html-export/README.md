# HTML Export - "The Correction"

This directory contains the complete novel "The Correction" exported to HTML format with chapter navigation.

## Files

- **index.html** - Table of contents with all chapters organized by parts
- **00-prologue.html** through **30-epilogue.html** - Individual chapter pages

## Features

### Navigation
- **Previous/Next buttons** on each chapter page
- **Table of contents** with all chapters organized by parts
- **Chapter information** showing POV, timeline, and word count
- **Responsive design** works on desktop, tablet, and mobile

### Styling
- **Clean, clinical theme** (white, grey and cold blue) matching the books
- **Print-friendly** CSS for printing chapters
- **Smooth transitions** and hover effects

## Usage

### Reading Online
1. Open `index.html` in any web browser
2. Click on any chapter to start reading
3. Use Previous/Next buttons to navigate between chapters

### Printing
- Open any chapter in a browser
- Use File → Print or Ctrl+P
- The print stylesheet will automatically apply

### Sharing
- The entire `html-export` directory can be zipped and shared
- All files are self-contained (no external dependencies)
- Works offline once downloaded

## Structure

### Prologue
The Conviction: Marcus is transferred to Ashford's Wing C

### Part One: The Erasure (Chapters 1–8)
Marcus is erased in two months; Kira arrives; the triplets, Tanaka and Isaiah are introduced

### Part Two: The Connection (Chapters 9–17)
Recognition, recovery, the secret message system, Project Continuity uncovered

### Part Three: The Plan (Chapters 18–22)
Allies inside the staff, the escape plan, Nikolai's solo session, Isaiah's choice to stay

### Part Four: The Storm (Chapters 23–26)
The fact storm, the breakout, the reunion with Elena, the pursuit

### Part Five: The Aftermath (Chapters 27–29)
Isaiah's article, recovery, the group splits up

### Epilogue
Seven Paths, One Truth: November 14, 2106, leading into "The Lost Hour"

## Statistics

- **Total Chapters**: 31 (Prologue + 29 chapters + Epilogue)
- **Total Word Count**: ~95,500 words
- **POV Characters**: 7 (Marcus, Kira, Dmitri, Alexei, Nikolai, Tanaka, Isaiah)
- **Timeline**: October 2105 – November 14, 2106

## Technical Details

- **Generated from**: Markdown source files
- **Template**: `templates/novel-export-template.html`
- **Script**: `scripts/export-novel-html.py`
- **Markdown processor**: Python markdown library

## Regenerating

To regenerate the HTML files:

```bash
python scripts/export-novel-html.py
```

Or use the batch file:

```bash
scripts/export-novel.bat
```

## Browser Compatibility

Tested and working on:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Notes

- All HTML files are self-contained
- No external CSS or JavaScript dependencies
- Images and fonts use system defaults
- Works completely offline
- Safe to host on any web server

---

**The Correction** - Novel 04 of the Histologic Series  
© 2025 - All Rights Reserved




