# "The Correction" - Ebook Guide

## 📚 Available Formats

### EPUB (Universal E-reader Format)
- **File**: `the-correction.epub`
- **Size**: ~139 KB
- **Compatible with**: 
  - Apple Books (iPad, iPhone, Mac)
  - Google Play Books
  - Kobo
  - Nook
  - Most e-readers (except Kindle)
  - Calibre
  - Adobe Digital Editions

### MOBI (Kindle Format)
- **File**: `the-correction.mobi` (after conversion)
- **Compatible with**:
  - Amazon Kindle devices
  - Kindle apps (iOS, Android, PC, Mac)

### HTML (Web Format)
- **Location**: `html-export/index.html`
- **Compatible with**: Any web browser
- **Features**: Chapter navigation, table of contents

---

## 🔄 Converting to Kindle Format

### Method 1: Using Calibre (Recommended)

1. **Install Calibre** (if not already installed)
   - Download from: https://calibre-ebook.com/
   - Install with default settings

2. **Convert using batch file**
   ```bash
   scripts\convert-novel-to-kindle.bat
   ```

3. **Or convert manually**
   ```bash
   ebook-convert the-correction.epub the-correction.mobi --output-profile kindle
   ```

### Method 2: Using Amazon's Send to Kindle

1. Email the EPUB file to your Kindle email address
2. Amazon will automatically convert it
3. Find your Kindle email: Amazon Account → Content & Devices → Preferences → Personal Document Settings

---

## 📖 Reading the Ebook

### On Kindle

**Option 1: USB Transfer**
1. Connect Kindle to computer via USB
2. Copy `the-correction.mobi` to Kindle's `documents` folder
3. Eject Kindle safely
4. Book appears in your library

**Option 2: Email to Kindle**
1. Email `the-correction.mobi` or `the-correction.epub` to your Kindle email
2. Subject: "Convert" (if sending EPUB)
3. Book appears on your Kindle within minutes

**Option 3: Calibre**
1. Open Calibre
2. Connect Kindle
3. Add book to Calibre library
4. Click "Send to device"

### On Apple Books (iPad/iPhone/Mac)

1. Open `the-correction.epub` file
2. It automatically opens in Apple Books
3. Book is added to your library

### On Android

1. Install Google Play Books or other EPUB reader
2. Open `the-correction.epub` file
3. Choose your reader app

### On Computer

**Option 1: Calibre**
1. Open Calibre
2. Add book to library
3. Double-click to read

**Option 2: Web Browser**
1. Open `html-export/index.html`
2. Read in browser with navigation

---

## 📝 Ebook Features

### Metadata
- **Title**: The Correction
- **Subtitle**: Novel 04 of the Histologic Series
- **Author**: Histologic Series
- **Language**: English
- **Chapters**: 27 (Prologue + 25 chapters + Epilogue)
- **Word Count**: ~49,500 words

### Formatting
- ✅ Proper chapter breaks
- ✅ Table of contents (clickable)
- ✅ Justified text
- ✅ Paragraph indentation
- ✅ Emphasis (italics) preserved
- ✅ Strong (bold) preserved
- ✅ Section breaks (horizontal rules)

### Navigation
- ✅ Full table of contents
- ✅ Chapter-by-chapter navigation
- ✅ Bookmarks supported
- ✅ Search functionality (device-dependent)

---

## 🔧 Regenerating the Ebook

If you edit the chapters and need to regenerate:

### Step 1: Regenerate EPUB
```bash
python scripts/create-novel-ebook.py
```

### Step 2: Convert to MOBI (optional)
```bash
scripts\convert-novel-to-kindle.bat
```

---

## 📊 File Sizes

- **EPUB**: ~139 KB (compressed)
- **MOBI**: ~200-250 KB (after conversion)
- **HTML Export**: ~500 KB (all 28 files)

---

## 🎯 Recommended Reading Order

### For First-Time Readers
1. Read the three short stories first (optional but recommended):
   - 01-the-believers-fall
   - 02-the-stolen-fact
   - 03-the-divided-truth
2. Then read "The Correction"

### For Series Readers
- This is Novel 04 in the Histologic Series
- Can be read standalone, but better with context from short stories

---

## 💡 Tips for Best Reading Experience

### On E-readers
- Adjust font size for comfort
- Use night mode for evening reading
- Bookmark favorite passages
- Use built-in dictionary for unfamiliar terms

### On Tablets/Phones
- Use reading apps with night mode
- Adjust brightness for comfort
- Enable page-turn animations
- Use split-screen for note-taking

### On Computer
- HTML version recommended for computer reading
- Better formatting and navigation
- Easier to reference while writing

---

## 🐛 Troubleshooting

### EPUB Won't Open
- **Solution**: Install a compatible reader (Calibre, Adobe Digital Editions)
- **Alternative**: Use HTML version in web browser

### MOBI Conversion Failed
- **Solution**: Install Calibre and ensure ebook-convert is in PATH
- **Alternative**: Email EPUB to Kindle email with subject "Convert"

### Formatting Issues
- **Solution**: Regenerate ebook with updated script
- **Alternative**: Use HTML version

### Missing Chapters
- **Solution**: Verify all 27 chapter files exist in `chapters/` directory
- **Alternative**: Regenerate from source

---

## 📧 Sharing the Ebook

### Legal Sharing
- Share with friends and family for personal use
- Do not distribute commercially
- Do not upload to public file-sharing sites

### Best Formats to Share
- **EPUB**: Most universal
- **MOBI**: For Kindle users specifically
- **HTML Export**: For web/computer reading

### How to Share
1. **Zip the files**:
   - For EPUB: Just send the .epub file
   - For complete package: Zip `04-the-correction` folder
2. **Email or cloud storage** (Dropbox, Google Drive, etc.)
3. **Include this guide** for recipients

---

## 🎉 Enjoy Reading!

"The Correction" is a complete novel with:
- 27 chapters
- ~49,500 words
- 8 POV characters
- Complete story arc
- Perfect setup for "The Lost Hour" (Novel 05)

**Happy reading!** 📚✨

---

## 📞 Support

For issues or questions:
- Check HTML version: `html-export/index.html`
- Verify source files in `chapters/` directory
- Regenerate ebook if needed
- Try alternative reading formats

---

**The Correction** - Novel 04 of the Histologic Series  
© 2025 - All Rights Reserved

