# Publishing Guide (EPUB, Kindle, KDP)

**Updated Sept 2026.** It replaces the old Kindle guides, which were Windows-only, MOBI-based and used outdated paths.

## 1. Build the Ebooks
Run from the `histologic/` directory (see `scripts/README.md`):
```bash
python3 scripts/create-ebook.py          # → novels/01-03-stories/histologic-stories.epub
python3 scripts/create-novel-ebook.py    # → novels/04-the-correction/the-correction.epub
python3 scripts/export-novel-html.py     # → novels/04-the-correction/html-export/index.html
```
Both builders use only the Python standard library. Before publishing, check each EPUB with **EPUBCheck** (the free W3C validator) or Calibre's viewer.

## 2. Reading on Your Own Kindle
- **Send to Kindle** (Amazon's app, web page or email) accepts **EPUB directly**. There's no need to convert. Send the `.epub` and it appears in your library.
- **Calibre**, if you want a local file for a sideloaded device: `ebook-convert the-correction.epub the-correction.azw3`. The command is `ebook-convert`; it is installed with Calibre. Prefer AZW3 or KFX to the obsolete MOBI format.

## 3. Publishing on Amazon KDP
1. Go to kdp.amazon.com and choose **Create → Kindle eBook**.
2. Fill in the metadata (section 5) and choose two categories, for example *Science Fiction → Dystopian* and *Science Fiction → Cyberpunk* (or *Short Stories* for the collection).
3. **Upload the EPUB.** KDP accepts EPUB, DOCX and KPF. It no longer accepts MOBI for ebooks.
4. Upload a cover (section 6) and check the result in the online Previewer.
5. Set the price and royalty. KDP's 70% royalty tier has applied to roughly $2.99–$9.99 list prices. **Check the current terms on KDP**, since they change.
6. **KDP Select or wide distribution:**
   - **Select** is 90 days exclusive to Amazon, with Kindle Unlimited page-read income and promotion days.
   - **Wide** is sold everywhere. Draft2Digital can distribute to Apple Books, Kobo and Barnes & Noble.

   A common approach is to start with Select for one 90-day term, then reassess.

## 4. Suggested Order of Release
1. *Histologic Stories* (the three short stories, ~17,500 words) as a low-price entry point.
2. *The Correction* (~95,500 words) as Book 1 of the novels.
3. Later books as they are rewritten. Keep the series name and numbering consistent on KDP ("Histologic, Book N").

## 5. Descriptions

### *Histologic Stories*
**Short:** Three stories from a future where history is science, truth is law, and doubt is a crime.

**Long:**
> In the future, history has become an exact science. Every fact is recorded, verified and broadcast straight into every citizen's mind. Nations are defined not by borders or language, but by which version of history they believe.
>
> **The Believer's Fall.** Marcus Chen has never questioned a fact in his life. When the woman he loves turns out to be an outlaw, he reports her, and the system convicts him anyway.
>
> **The Stolen Fact.** Kira Osman helped build the Factorepo Spire. When a fact she entered herself vanishes from the record, she reports it, and becomes the suspect.
>
> **The Divided Truth.** In the fog of a border zone where two nations' histories collide, an enforcer hunts an outlaw, and a technician is caught between them. They are brothers. They are triplets. And what the system can't take from them is each other.

### *The Correction*
**Short:** They erased him in two months. They didn't expect anyone to bring him back.

**Long:**
> Marcus Chen did everything the system asked, and it sent him to Ashford anyway, to a silent wing of glass cells where a programme called Continuity takes the belief out of people and leaves them empty.
>
> Seven prisoners have been chosen: a believer, an architect of the record, three brothers who cannot be broken, a doctor, and a journalist. To survive they must learn to look erased while staying themselves, find each other without speaking, and escape a building that can read their minds, before the day they are due to be finished.
>
> A psychological thriller about memory, certainty, and the cost of being free.

**Keywords:** dystopian thriller, surveillance, memory, mind control, prison escape, philosophical science fiction, alternate future.

## 6. Covers
- **Size:** 1600 × 2560 px (a 1.6:1 ratio). **Readable as a thumbnail** at about 80 × 120 px.
- **Style:** clean and clinical, matching the books: white, gray and cold blue, with one accent colour. **Not steampunk.** Motifs: glass cells, a white room, a flickering building, a hand pressed to glass.
- **Options:** DIY with a template tool, a pre-made cover, or a commissioned designer. Keep the series look consistent across books.

## 7. Before You Publish
- [ ] EPUBCheck passes, and the table of contents works on a real device
- [ ] Title, series name, book number and author are consistent
- [ ] No placeholder text or notes left in the chapters
- [ ] No copyrighted lyrics (see `PROJECT-RULES.md` §5)
- [ ] The cover reads clearly as a thumbnail
