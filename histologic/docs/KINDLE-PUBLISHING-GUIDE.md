# Kindle Publishing Guide - Histologic Stories

## Quick Start

### Step 1: Create EPUB
```bash
python scripts/create-ebook.py
```

This creates `histologic-stories.epub` in your project root.

### Step 2: Convert to Kindle Format

**Option A: Using Calibre (Free, Recommended)**
```bash
calibre-convert histologic-stories.epub histologic-stories.mobi
```

**Option B: Using Amazon Kindle Previewer (Free)**
1. Download from: https://www.amazon.com/Kindle-Previewer/b?node=21381691011
2. Open `histologic-stories.epub` in Kindle Previewer
3. It will automatically convert to KPF format
4. Export as MOBI or upload EPUB directly to KDP

**Option C: Upload EPUB directly to KDP**
- Amazon KDP now accepts EPUB files directly
- They'll convert it automatically

## What Gets Created

### EPUB Contents
- **Title Page**: Beautiful cover page with book title
- **Copyright Page**: Copyright and publication info
- **Table of Contents**: Interactive navigation
- **Three Stories**:
  1. The Believer's Fall (~4,745 words)
  2. The Stolen Fact (~4,445 words)
  3. The Divided Truth (~7,918 words)
- **About Page**: Introduction to the Histologic universe

### Total Book Stats
- **Total Words**: ~17,000 words
- **Reading Time**: ~85 minutes
- **Print Pages**: ~60-70 pages (estimated)
- **Genre**: Science Fiction / Dystopian

## Publishing Options

### Option 1: Amazon Kindle Direct Publishing (KDP)

**Pros:**
- Largest ebook market
- 70% royalty option
- Kindle Unlimited enrollment
- Professional platform

**Steps:**
1. Go to https://kdp.amazon.com
2. Create account / Sign in
3. Click "Create New Title"
4. Fill in metadata:
   - **Title**: Histologic Stories: Three Tales from a Future Where History is Science
   - **Subtitle**: (optional) The Believer's Fall, The Stolen Fact, The Divided Truth
   - **Author**: Your name
   - **Description**: See below
   - **Keywords**: science fiction, dystopia, short stories, philosophy, future, AI, surveillance
   - **Categories**: Science Fiction > Dystopian, Science Fiction > Short Stories
5. Upload `histologic-stories.epub` or `.mobi`
6. Set pricing (e.g., $2.99 for 70% royalty)
7. Preview using online previewer
8. Publish!

**Recommended Price Points:**
- $0.99 - $2.99: 35% royalty
- $2.99 - $9.99: 70% royalty (recommended: $2.99 - $4.99)

### Option 2: Draft2Digital

**Pros:**
- Distributes to multiple platforms (Apple Books, Kobo, Barnes & Noble, etc.)
- Free to use
- Automatic conversion

**Steps:**
1. Go to https://www.draft2digital.com
2. Create account
3. Upload EPUB
4. Set metadata
5. Choose distribution channels
6. Publish

### Option 3: Direct Sales

**Pros:**
- Keep 100% of revenue
- Full control
- Direct relationship with readers

**Options:**
- Gumroad
- Payhip
- Your own website

## Book Description (for KDP)

### Short Description (160 characters)
```
Three interconnected stories from a future where history is science, truth is law, and doubt is crime. Welcome to the Histologic universe.
```

### Full Description
```
In a future Earth, history has become an exact science. Massive databases called factorepos store every historical fact, verified for logical consistency and used as the foundation for all truth, law, and governance. Nations are defined not by borders or language, but by which version of history they believe.

This collection contains three interconnected short stories set in the Histologic universe:

THE BELIEVER'S FALL
Marcus Chen is a true believer in the system. When he falls in love with a beautiful woman named Elena, he doesn't know she's an outlaw recruiter sent to seduce him. Despite remaining faithful to his beliefs, he's deemed compromised and sent to a correctional facility where minds are rebuilt.

THE STOLEN FACT
Kira Osman is meticulous about recording facts. When a fact she's certain she input mysteriously vanishes from the factorepo, her investigation leads her down a dangerous path. The system she trusted is hiding something, and discovering the truth will cost her everything.

THE DIVIDED TRUTH
Three men in the border zone between warring nations: an enforcer hunting an outlaw, the outlaw he's hunting, and a technician caught between them. Only in the story's climax is it revealed that these three men are identical triplets, torn apart by their father's death and driven to opposite extremes. All three will end up in the same correctional facility, but their connection may prove impossible to break.

Explore a world where:
• Truth is absolute and doubt is crime
• The past controls the future
• History is weaponized
• Freedom and certainty cannot coexist

Perfect for fans of 1984, Black Mirror, and philosophical science fiction.

Total length: ~17,000 words (approximately 60-70 print pages)
```

## Cover Design

### DIY Cover Options

**Option 1: Canva (Free/Paid)**
1. Go to canva.com
2. Search for "Kindle Book Cover" template
3. Dimensions: 1600 x 2560 pixels (recommended)
4. Design elements:
   - Dark, futuristic theme
   - Title: "HISTOLOGIC"
   - Subtitle: "Stories from a Future Where History is Science"
   - Author name
   - Minimalist, tech-inspired design

**Option 2: DIY Book Covers (Paid)**
- https://diybookcovers.com
- Pre-made templates
- $30-80

**Option 3: Hire a Designer**
- Fiverr: $50-200
- 99designs: $299+
- Reedsy: $500+

### Cover Design Tips
- Keep it simple and bold
- Title should be readable as thumbnail
- Dark, futuristic aesthetic
- Avoid clutter
- Test as small thumbnail (80x120px)

## Pricing Strategy

### Recommended Pricing

**Launch Price**: $0.99 (build reviews)
- Run for 2-4 weeks
- Encourage reviews
- Build momentum

**Regular Price**: $2.99 - $3.99
- 70% royalty tier
- Competitive for short story collection
- Good value for readers

**Special Promotions**:
- Free days (if in KDP Select)
- Countdown deals
- $0.99 promotions

### Royalty Calculation

At $2.99:
- 70% royalty = $2.09 per sale
- 35% royalty = $1.05 per sale

At $3.99:
- 70% royalty = $2.79 per sale

## Marketing Ideas

### Pre-Launch
1. Build email list
2. Create social media presence
3. Share excerpts
4. Build anticipation

### Launch
1. Announce on social media
2. Email your list
3. Ask for reviews
4. Submit to book promotion sites

### Post-Launch
1. Continue gathering reviews
2. Run promotions
3. Write more stories
4. Build series

### Promotion Sites
- BookBub (expensive but effective)
- Freebooksy / Bargain Booksy
- Robin Reads
- Book Gorilla
- Many Books

## KDP Select vs. Wide Distribution

### KDP Select (Exclusive to Amazon)

**Pros:**
- Kindle Unlimited (readers pay subscription, you get paid per page read)
- Free promotion days (5 per 90 days)
- Countdown deals
- Higher visibility in Amazon

**Cons:**
- Exclusive to Amazon (can't sell elsewhere)
- 90-day commitment

**Recommendation**: Start with KDP Select for first 90 days, then evaluate.

### Wide Distribution (All Platforms)

**Pros:**
- Reach more readers
- Not dependent on one platform
- Apple Books, Kobo, Nook, etc.

**Cons:**
- No Kindle Unlimited
- More complex management

## Technical Requirements

### EPUB Specifications
- ✓ EPUB 3.0 format
- ✓ Reflowable text
- ✓ Table of contents
- ✓ Proper metadata
- ✓ CSS styling
- ✓ Valid XHTML

### Kindle Requirements
- File size: < 50 MB (our EPUB is ~50 KB)
- Format: EPUB, MOBI, or KPF
- DRM: Optional (not recommended)

### Cover Requirements
- Minimum: 1000 x 1600 pixels
- Recommended: 1600 x 2560 pixels
- Maximum: 10,000 pixels on longest side
- Format: JPEG or TIFF
- Color: RGB
- Resolution: 72 dpi minimum

## Quality Checklist

Before publishing, verify:

- [ ] EPUB validates (use EPUBCheck)
- [ ] Preview on multiple devices
- [ ] Table of contents works
- [ ] No formatting issues
- [ ] Metadata is complete
- [ ] Cover looks good as thumbnail
- [ ] Description is compelling
- [ ] Keywords are relevant
- [ ] Categories are appropriate
- [ ] Price is set correctly
- [ ] Author bio is complete

## Testing Your EPUB

### Validation
```bash
# Install EPUBCheck (requires Java)
java -jar epubcheck.jar histologic-stories.epub
```

### Preview Tools
1. **Calibre** (Free) - Best for desktop preview
2. **Kindle Previewer** (Free) - Amazon's official tool
3. **Adobe Digital Editions** (Free) - Standard EPUB reader
4. **Apple Books** (Mac) - Preview on Apple devices
5. **Google Play Books** (Free) - Upload and preview

### Test Devices
- Kindle (various models)
- iPad / iPhone
- Android tablet / phone
- E-ink readers (Kobo, Nook)

## Common Issues & Fixes

### Issue: Cover doesn't display
**Fix**: Ensure cover is JPEG, correct dimensions, and referenced in OPF

### Issue: Table of contents broken
**Fix**: Check that all files are referenced correctly in toc.ncx and nav document

### Issue: Formatting looks wrong
**Fix**: Preview in multiple readers, adjust CSS for compatibility

### Issue: File too large
**Fix**: Optimize images, remove unnecessary files

## Updating Your Book

After publishing, you can update:
1. Go to KDP Bookshelf
2. Click "..." next to your book
3. Select "Edit eBook content"
4. Upload new file
5. Republish

Changes go live within 72 hours.

## Building a Series

### Future Books
1. **Histologic Stories Volume 2** - Three more stories
2. **The Correctional Facility** - Novel-length story
3. **The Fact Wars** - Border conflict novel
4. **The Outlaw Network** - Resistance novel

### Series Benefits
- Readers buy multiple books
- Build loyal fanbase
- Cross-promotion
- Increased visibility

## Legal Considerations

### Copyright
- You own the copyright
- Register with US Copyright Office (optional but recommended)
- Include copyright notice in book

### ISBN
- Not required for Kindle
- Amazon provides free ASIN
- ISBN needed for print or wide distribution

### Taxes
- Provide tax information to Amazon
- Track income for tax purposes
- Consider business entity (LLC, etc.)

## Resources

### Tools
- **Calibre**: Free ebook management and conversion
- **Kindle Previewer**: Amazon's preview tool
- **EPUBCheck**: Validate EPUB files
- **Canva**: Cover design
- **Grammarly**: Proofreading

### Learning
- **KDP Help**: https://kdp.amazon.com/help
- **Kboards**: Writer's Cafe forum
- **r/selfpublish**: Reddit community
- **The Creative Penn**: Podcast and blog
- **David Gaughran**: Marketing expert

### Services
- **Reedsy**: Find editors, designers, formatters
- **Fiverr**: Affordable freelancers
- **BookBrush**: Marketing graphics
- **Written Word Media**: Book promotion

## Next Steps

1. **Create EPUB**: Run `python scripts/create-ebook.py`
2. **Test EPUB**: Open in Calibre and Kindle Previewer
3. **Create Cover**: Design or commission a cover
4. **Set Up KDP Account**: Register at kdp.amazon.com
5. **Upload and Publish**: Follow KDP wizard
6. **Market**: Share with friends, social media, email list
7. **Gather Reviews**: Ask readers for honest reviews
8. **Write More**: Continue the Histologic series!

---

**Questions?** Check the scripts/README-EXPORT.md for technical details.

**Ready to publish?** Run: `python scripts/create-ebook.py`

Good luck with your Kindle publishing journey!

