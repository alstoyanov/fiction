# The Correction (Novel 04)

The first full novel in the Histologic series. It continues directly from the three short stories (*The Believer's Fall*, *The Stolen Fact*, *The Divided Truth*) and leads into *The Lost Hour* (Novel 05).

**Genre:** Psychological thriller / prison escape
**Length:** ~95,500 words: Prologue, 29 chapters, Epilogue
**Timeline:** October 2105 – November 14, 2106
**POV characters:** Marcus, Kira, Dmitri, Alexei, Nikolai, Tanaka, Isaiah
**Status:** First draft complete (rewrite, Sept 2026)

## Premise
Marcus Chen reported the outlaw he loved and was convicted anyway. At Ashford Correctional Facility, a programme called Project Continuity erases him in two months. Seven prisoners have been chosen as test subjects, one of each "resistant" kind of mind. They learn to look erased while staying themselves, find each other without speaking, and escape during a fact storm they create, a day before they are due to be finished.

## Files

| Path | Contents |
|------|----------|
| `chapters/` | The novel: `00-prologue.md` … `30-epilogue.md` |
| `chapters-summaries/` | One summary per chapter, plus a `README.md` with the canon decisions, timeline, cast, the three twists and the fact-storm rules |
| `html-export/` | Generated HTML with chapter navigation (open `index.html`) |
| `the-correction.epub` | Generated EPUB |
| `../../plots/04-the-correction-REVISED.md` | The plot outline (v2) |

`chapters-summaries/README.md` is the reference to check before editing the chapters: it records every decision that ties the novel to the short stories and to Book 5.

## Structure
- **Prologue: The Conviction**
- **Part One: The Erasure** (Ch 1–8)
- **Part Two: The Connection** (Ch 9–17)
- **Part Three: The Plan** (Ch 18–22)
- **Part Four: The Storm** (Ch 23–26)
- **Part Five: The Aftermath** (Ch 27–29)
- **Epilogue: Seven Paths, One Truth**

## Building the HTML and EPUB
Run these from the `histologic/` directory:

```
python3 scripts/export-novel-html.py
python3 scripts/create-novel-ebook.py
```

Both scripts use only the Python standard library. The HTML exporter uses the `markdown` package if it is installed. The chapter list and parts are defined in `PARTS` at the top of each script, so update both if you rename or add a chapter.

**Kindle:** convert the EPUB with Calibre, `ebook-convert the-correction.epub the-correction.azw3`, or send the EPUB directly with Amazon's Send to Kindle, which accepts EPUB.

## Known Open Items
- There has not yet been a full continuity read-through of the draft in one sitting.
- The possible hint in Chapter 19 that Elena's technician at the regional node is Adrian Kovač is deliberately ambiguous. Keep it or cut it when Book 6 is rewritten.
