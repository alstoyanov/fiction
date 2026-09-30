# Build Scripts

All scripts use **only the Python standard library**. The HTML exporter uses the `markdown` package if it is installed, and falls back to a built-in converter if not. The examples assume you run from `histologic/`.

| Script | Output |
|--------|--------|
| `create-all-epubs.py` | Runs everything below, in order. Works from any directory. |
| `create-ebook.py` | `novels/01-03-stories/histologic-stories.epub`: the three short stories |
| `export-story-html.py <folder>` or `--all` | `novels/01-03-stories/<story>/<story>.html`, using `templates/story-export-template.html` |
| `create-novel-ebook.py` | One EPUB per novel (`the-correction.epub`, `the-lost-hour.epub`, `the-distributed-truth.epub`): title page, part dividers, chapters, and an NCX table of contents for older readers. Pass `04`, `05` or `06` to build one book |
| `export-novel-html.py` | `html-export/` in each novel folder: one page per chapter plus `index.html`, using `templates/novel-export-template.html`. Pass `04`, `05` or `06` to build one book |
| `novels_config.py` | Shared book list for the two novel scripts: folder, title, blurb, and the chapter order grouped by part. Add a book here to build it |

```bash
python3 scripts/create-all-epubs.py          # build everything
python3 scripts/create-novel-ebook.py        # just the Book 4 EPUB
python3 scripts/export-story-html.py --all   # just the story HTML pages
```

## Adding or Renaming Chapters (Book 4)
The chapter list, parts and POVs are defined in `PARTS` at the top of **both** `create-novel-ebook.py` and `export-novel-html.py`. Update both.

## Adding Books 5–9
When a book is rewritten, copy the two Book 4 scripts, or make them take a novel folder. Then add the new steps to `STEPS` in `create-all-epubs.py`. (The old `ebooklib`-based builders for the pre-rewrite drafts were removed.)

## Checking
- Validate EPUBs with EPUBCheck, or open them in Calibre.
- Publishing and Kindle: `docs/PUBLISHING.md`.
