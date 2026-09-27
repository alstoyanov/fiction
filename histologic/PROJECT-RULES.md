# Histologic: Project Rules

**Version 2.0, Sept 2026.** It replaces the Nov 2025 rules, which were built around full/concise document pairs.

---

## 1. Folder Structure
```
histologic/
├── README.md                 # Front page: concept, books, where things are
├── PROJECT-RULES.md          # This file
├── SERIES-OVERVIEW.md        # All nine books: canon (1–5) and provisional (6–9)
├── basic-idea.txt            # The founding concept (never edited)
├── worldbuilding/            # Canon world reference: core-system, nations, society, fact-storms, interfaces-and-correction
├── characters/               # Character files (the Sept 2026 rewrites are current; the rest are pre-rewrite)
├── plots/                    # Plot outlines, one full + one concise per book; 00-FOUNDATION-MANUSCRIPT.md
├── novels/
│   ├── 01-03-stories/        # The three short stories (+ collection EPUB)
│   ├── 04-the-correction/    # chapters/, chapters-summaries/, html-export/, the-correction.epub
│   └── 05-…09-…/             # Pre-rewrite drafts (to be replaced book by book)
├── templates/                # Character, plot and export templates
├── scripts/                  # HTML/EPUB builders (see scripts/README.md)
└── docs/                     # Publishing guide
```

## 2. Order of Authority (Canon)
When sources disagree, **the earlier one wins**:
1. `basic-idea.txt`
2. The short stories (`novels/01-03-stories/*/story.md`)
3. *The Correction*: the chapters, plus `chapters-summaries/README.md` for its canon decisions
4. *The Lost Hour*: `plots/05-the-lost-hour-full.md`, later the book itself
5. `plots/00-FOUNDATION-MANUSCRIPT.md` and the character files rewritten since Sept 2026
6. `worldbuilding/`, a summary of all of the above. If it disagrees with them, fix the summary.

**The series is being rewritten in order.** A newer book must fit the older ones, never the other way round. Plots and drafts for books not yet rewritten (6–9) are **not binding**. Use them as sources of ideas.

## 3. Rewrite Workflow (per book)
1. **Plot:** revise the full and concise outlines. Check them against every earlier book and the manuscript plan. Give the book **two or three real twists** with fair clues (a clue map), not a predictable arc.
2. **Summaries:** one file per chapter, plus a `chapters-summaries/README.md` covering canon decisions, timeline, cast, twists and rules.
3. **Chapters:** draft **one part at a time**, then pause for review.
4. **Check:** weekdays against the calendar, ages against the character files, headcounts, and cross-references.
5. **Build:** HTML and EPUB (`scripts/README.md`).
6. **Clean up:** delete status and progress logs for the book once it's done. Git keeps the history. No `*-COMPLETE.md` files.

## 4. Canon Rules That Are Easy to Break
- **Fact storms are neural and perceptual.** The physical world never changes. No meteorological language. The Lake Erie fog is real weather.
- **Removing an interface kills.** Spoofing telemetry is the only way out of tracking. A spoofed person still receives broadcasts.
- **The Judge works in probabilities** about people (over 60% means corrective custody). There is no appeal, until the Lost Hour Doctrine (Book 5).
- **Citizens believe facts are immutable,** but insiders can delete or adjust them through the hidden "true source" (Principle Three).
- **Neutral zones are claimed by both nations,** not lawless.
- **Correction is sincere** below the very top. It is done by kind people who believe it heals.
- **The nations were designed:** in the official story they are histobranches, and in truth they are engineered rivals. Nobody knows this before the manuscript reveals it.
- **The manuscript reveal schedule** (`00-FOUNDATION-MANUSCRIPT.md` §5) is binding. Characters may guess ahead of it, but not know.

## 5. Style
- **Aesthetic:** clean, clinical, ordered, the way the short stories are written. **Not steampunk**: no brass, gears, steam or gaslight.
- **POV:** close third person, one POV character per chapter. The voices are distinct: Dmitri is formal and avoids contractions, Alexei is warm, Tanaka writes clinical case notes, Isaiah has his memory palace, Marcus thinks in fact entries.
- **Songs:** only original lyrics written for the series, or public-domain pieces. **No real-world copyrighted songs**, not even named. See `characters/main-characters/protagonists/old-songs-character.md`.
- **Dates in chapter headers:** an italic dateline under each chapter title.
- **Section breaks:** `---`.

## 6. Naming
- **Never reuse a first name** within the cast. The old drafts had four Elenas and two Adrians. Check the character files and `SERIES-OVERVIEW.md` §4 before naming anyone.
- Surnames may repeat only when it is deliberate (a family) or explained ("Petrov is a common name").

## 7. Worldbuilding Principles
1. Logical consistency: no fact may contradict another.
2. Plausibility: technology is theoretically possible, and people behave like people.
3. Conflict potential: every system has built-in tensions.
4. Scale: concepts work at personal, national and world level.
5. Every element answers these questions: *How can this go wrong? Who benefits? Who is harmed? What happens at the edges? What do people fight about?*

## 8. Craft Reminders
- **Surveillance is central.** Show how it shapes every choice, and justify any moment of privacy (a blind spot, an unmonitored space and its cost).
- **Show The Judge's limits.** It can't see intention, love or what isn't recorded.
- **Correction is complex and costly,** for the corrected and the correctors alike.
- **The wider world** (other nations and borders) should be felt even in Veridica-bound books.

## 9. Before Adding or Changing Canon
- [ ] Does it contradict an earlier source (section 2)?
- [ ] Does it fit the world's technology and its social structure?
- [ ] Are the dates, ages and weekdays checked?
- [ ] Is the name unique?
- [ ] Are the relevant `worldbuilding/`, character and plot files updated?
- [ ] Does it create story potential?

## 10. Working With AI Assistance
- **Load order for a session:**
  1. `README.md` and this file.
  2. `worldbuilding/README.md` (it indexes the rest).
  3. The current book's `chapters-summaries/README.md` and plot.
  4. The relevant character files.
- Ask for a contradiction check against the order of authority before finalising anything.
- Nothing is committed unless the author asks.
