# HTML Export - "The Correction"

This directory contains the complete novel "The Correction" exported to HTML format with chapter navigation.

## Files

- **index.html** - Table of contents with all chapters organized by parts
- **00-prologue.html** through **26-epilogue.html** - Individual chapter pages

## Features

### Navigation
- **Previous/Next buttons** on each chapter page
- **Table of contents** with all chapters organized by parts
- **Chapter information** showing POV, timeline, and word count
- **Responsive design** works on desktop, tablet, and mobile

### Styling
- **Steampunk/brass theme** matching the Histologic aesthetic
- **Dark background** for comfortable reading
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

### Part One: The Gathering (8 chapters)
Prologue + Chapters 1-7 - All eight inmates introduced

### Part Two: The Cracks (7 chapters)
Chapters 8-14 - Evidence gathered, relationships deepened

### Part Three: The Plan (4 chapters)
Chapters 15-18 - Final preparations and successful escape

### Part Four: The Storm (4 chapters)
Chapters 19-22 - Aftermath, pursuit, network building

### Part Five: The Divergence (3 chapters)
Chapters 23-25 - Publication, love, mission established

### Epilogue
Chapter 26 - Seven paths, setup for "The Lost Hour"

## Statistics

- **Total Chapters**: 27 (Prologue + 25 chapters + Epilogue)
- **Total Word Count**: ~49,500 words
- **POV Characters**: 8 (rotating perspectives)
- **Timeline**: August 1 - November 15, 2106

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



