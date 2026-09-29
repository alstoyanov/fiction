# Mytholore

**Mytholore** is a metal project that makes **concept albums based on the world's mythologies**. Each album tells one myth or cycle of myths from start to finish. The lyrics and music are generated with AI: music with **Suno**, cover art with several image models. The concept, the research, the writing and the final choices are ours.

This folder holds everything behind each album: the mythological research, the story arc, the lyrics, the Suno prompts, the cover-art prompts and the release texts.

---

## The Band's Sound
Mytholore is **power, heavy and symphonic metal**, not death or doom. The touchstones are classic power metal with epic choirs and galloping speed, anthemic heavy metal, classic 70s–80s heavy rock and metal with a big voiced lead singer, and symphonic metal with operatic female vocals.
- **Vocals:** clean and powerful. A soaring or gritty male lead, an operatic female voice for goddesses and narrators, and big choirs on the choruses. **No growls, no screamed vocals.**
- **Sound:** full and dramatic. A full orchestra, twin lead guitars, galloping double bass, keyboards, and a guitar solo in most songs.
- **Tempo:** mostly mid-to-fast (110–180 bpm). A slow track is rare and has to earn its place.
- **Folk colour:** each mythology adds its own traditional instruments on top (see the mythology README).
- **In Suno:** never name real bands. Describe the sound instead, and use the default exclude list in `guides/suno.md`.

## Folder Structure

```
mytholore/
├── README.md                  ← this file
├── .gitignore                 ← keeps large audio/image masters out of git
├── guides/                    ← how we work (applies to every album)
│   ├── workflow.md            ← idea → research → lyrics → Suno → art → release
│   ├── lyrics.md              ← lyric style, structure tags, voice
│   ├── suno.md                ← style prompts, metatags, versions, what to record
│   └── cover-art.md           ← art direction, prompt format, per-model notes
├── _templates/                ← copy these to start something new
│   ├── mythology/             ← a new mythology folder (README + album-ideas.md)
│   └── album/                 ← a new album folder (README, lore, tracks, art, release)
└── mythologies/
    ├── README.md              ← index of every mythology and album, with status
    └── <mythology>/           ← e.g. norse/, egyptian/, yoruba/, aztec/
        ├── README.md          ← the mythology: sources, themes, sound, album list
        └── <NN-album-slug>/   ← e.g. 01-ragnarok/
            ├── README.md      ← concept, tracklist, status, credits, links
            ├── lore.md        ← the myth, characters, sources, story arc
            ├── tracks/
            │   └── NN-track-slug.md   ← story · Suno style · Suno lyrics · cover prompt
            ├── art/
            │   ├── cover-prompts.md   ← prompts, models, seeds, chosen image
            │   └── (cover images)
            └── release/
                └── release-notes.md   ← descriptions, tags, platform links
```

## Naming Rules
- **Folders and files:** lowercase kebab-case (`the-twilight-of-the-gods`), with no spaces or special characters.
- **Mythology folders:** name them after the tradition, not the region: `norse`, `greek`, `celtic-irish`, `slavic`, `egyptian`, `mesopotamian`, `yoruba`, `aztec`, `inca`, `lakota`. Use a hyphenated qualifier when one region has several traditions (`celtic-irish`, `celtic-welsh`).
- **Album folders:** a two-digit number in release order *within that mythology*, then the slug: `01-ragnarok`, `02-the-voyage-of-bran`.
- **Track files:** the track number, then the slug: `03-the-wolf-is-loosed.md`.
- **Album titles** in the README may use any capitalisation and diacritics (*Ragnarǫk*). Slugs stay plain ASCII.

## Starting Something New
1. **A new mythology:** copy `_templates/mythology/` to `mythologies/<mythology>/` and fill in its README. Add a row to `mythologies/README.md`.
2. **A new album:** copy `_templates/album/` to `mythologies/<mythology>/<NN-album-slug>/`. Fill in `README.md` and `lore.md` **before** writing any lyrics. Then add the album to the mythology's README and to the index.
3. Follow `guides/workflow.md` from there.

## Moving Existing Albums In
For each album you've already released or drafted:
1. Create the mythology folder (if it doesn't exist yet) and the album folder from the templates.
2. Make one `tracks/NN-*.md` file per song, with its four parts:
   - the **story behind the song**;
   - the **Suno style** you actually used;
   - the **lyrics** as you pasted them into Suno;
   - the song's **cover art prompt**.

   Add the link to the version you kept in the optional log.
3. Put the cover prompt and the chosen image in `art/`.
4. Put the release description and platform links in `release/release-notes.md`.
5. Set the album's **Status** to `Released` and fill in the release date.

Anything you no longer have (for example, a lost prompt) gets written as `unknown`, so the gap is visible.

## What Every Track File Contains
Each song is one markdown file with four parts, in this order:
1. **Story behind the song:** two to three paragraphs on what actually happens in the myth at that point, as the sources tell it.
2. **Suno style:** the exact text for Suno's style field.
3. **Lyrics (optimised for Suno):** the exact text for Suno's lyrics field, with metatags and phonetic respellings.
4. **Cover art prompt:** the image prompt for that song's single or track art.

An optional generation log sits at the bottom. The template is `_templates/album/tracks/00-track-template.md`.

## Status Values
Use these consistently in every README and in the index:
`Idea` → `Researching` → `Writing` → `Generating` → `Art` → `Mastering` → `Released` (or `Shelved`).

## Principles
- **Respect the source.** Each album is based on real mythological material, and its sources are listed in `lore.md`. We retell the myth; we don't invent a "new" one and label it as tradition. Where we take liberties, `lore.md` says so.
- **Living traditions deserve extra care.** Some mythologies are still practised religions (for example Yoruba, Hindu, Shinto, and many Indigenous traditions of the Americas). For those, read `guides/lyrics.md` §Sensitivity before writing.
- **One album, one story.** Every track moves the story forward. The album README states the arc in a paragraph.
- **Record what the AI did.** Keep the prompt, model and version that produced each kept result, so the sound and look can be reproduced and stay consistent across albums.
