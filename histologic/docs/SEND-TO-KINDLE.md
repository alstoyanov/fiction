# Send to Kindle - Quick Guide

## Three Ways to Get Your Book on Kindle

### Method 1: Upload to Amazon KDP (Best for Publishing)

**If you want to sell your book:**

1. Go to https://kdp.amazon.com
2. Create account / Sign in
3. Click "Create" → "Kindle eBook"
4. Upload `histologic-stories.epub` (yes, EPUB works!)
5. Amazon converts it automatically
6. Preview and publish

**Result**: Book available for sale on Amazon

---

### Method 2: Email to Your Kindle (Best for Personal Use)

**If you just want to read it yourself:**

1. **Find your Kindle email address:**
   - Go to https://www.amazon.com/mycd
   - Look for "Send-to-Kindle Email Settings"
   - Your Kindle email looks like: `yourname@kindle.com`

2. **Convert EPUB to MOBI:**
   - Install Calibre: https://calibre-ebook.com
   - Run: `scripts\convert-to-kindle.bat`
   - Or manually: `ebook-convert histologic-stories.epub histologic-stories.mobi`

3. **Email the MOBI file:**
   - From your approved email (check Amazon settings)
   - To: `yourname@kindle.com`
   - Subject: (anything)
   - Attach: `histologic-stories.mobi`
   - Send!

4. **Book appears on your Kindle** (within minutes if connected to WiFi)

---

### Method 3: USB Transfer (Works Offline)

**If you have a USB cable:**

1. **Convert to MOBI:**
   ```bash
   scripts\convert-to-kindle.bat
   ```

2. **Connect Kindle to computer via USB**

3. **Copy file:**
   - Open Kindle drive
   - Go to `documents` folder
   - Copy `histologic-stories.mobi` there

4. **Eject Kindle safely**

5. **Book appears in your library!**

---

## Install Calibre (Free)

**Download**: https://calibre-ebook.com

**Windows Installation:**
1. Download installer
2. Run installer
3. Follow prompts
4. Restart computer (for command-line tools)

**After Installation:**
- Run `scripts\convert-to-kindle.bat` to convert
- Or use Calibre GUI to convert and manage books

---

## Quick Conversion Commands

### Using Calibre Command Line:
```bash
# Convert EPUB to MOBI
ebook-convert histologic-stories.epub histologic-stories.mobi --output-profile kindle

# Convert EPUB to AZW3 (newer format)
ebook-convert histologic-stories.epub histologic-stories.azw3 --output-profile kindle
```

### Using Our Batch File:
```bash
scripts\convert-to-kindle.bat
```

---

## Troubleshooting

### "Calibre not found"
- Install Calibre from https://calibre-ebook.com
- Restart your computer
- Try again

### "Email not working"
- Check your Kindle email at https://www.amazon.com/mycd
- Make sure you're sending from an approved email address
- Add your email to approved list in Amazon settings
- File must be MOBI format (not EPUB)

### "Book not appearing on Kindle"
- Make sure Kindle is connected to WiFi (for email method)
- Check "All" items in your Kindle library (not just "Downloaded")
- Sync your Kindle: Settings → Sync
- Wait a few minutes and check again

### "Conversion failed"
- Make sure EPUB file exists: `histologic-stories.epub`
- Try using Calibre GUI instead of command line
- Check that EPUB is valid

---

## Which Method Should I Use?

### For Personal Reading:
→ **Email to Kindle** (easiest, wireless)

### For Selling/Publishing:
→ **Upload to KDP** (Amazon converts automatically)

### For Offline/No Internet:
→ **USB Transfer** (works without WiFi)

### For Testing Before Publishing:
→ **Email to Kindle** (test on actual device first)

---

## File Formats Explained

- **EPUB**: Universal ebook format (most e-readers)
- **MOBI**: Older Kindle format (works on all Kindles)
- **AZW3**: Newer Kindle format (better formatting)
- **KPF**: Kindle Print Replica (for fixed-layout books)

**For Kindle, use MOBI** - it works on all Kindle devices and apps.

---

## Amazon KDP vs. Personal Use

### Amazon KDP (Publishing):
- ✓ Sell your book
- ✓ Reach millions of readers
- ✓ Earn royalties (35% or 70%)
- ✓ Professional distribution
- ✓ Upload EPUB directly (they convert)

### Personal Use (Email/USB):
- ✓ Read on your own Kindle
- ✓ Share with family (personal use only)
- ✓ Test before publishing
- ✓ No cost
- ✗ Can't sell or distribute widely

---

## Quick Start

**Just want to read it on your Kindle?**

1. Install Calibre: https://calibre-ebook.com
2. Run: `scripts\convert-to-kindle.bat`
3. Email `histologic-stories.mobi` to your Kindle email
4. Done!

**Want to publish and sell it?**

1. Go to https://kdp.amazon.com
2. Upload `histologic-stories.epub`
3. Set price and details
4. Publish!

---

## Need Help?

- **Calibre Help**: https://manual.calibre-ebook.com
- **KDP Help**: https://kdp.amazon.com/help
- **Send to Kindle**: https://www.amazon.com/sendtokindle
- **Kindle Email Settings**: https://www.amazon.com/mycd

---

**Ready to convert?**

Run: `scripts\convert-to-kindle.bat`

Or install Calibre and use the GUI for more control.

