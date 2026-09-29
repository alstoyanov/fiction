# Workflow: From Myth to Release

Each step leaves something behind in the album folder, so the album can be picked up or reproduced later.

| # | Step | Output | Status after |
|---|------|--------|--------------|
| 1 | **Choose the myth.** Pick one story or cycle that has a clear arc and enough drama for 8–12 songs. | A row in `mythologies/README.md` and the mythology's album list | `Idea` |
| 2 | **Research.** Read the primary sources, and note names, places, pronunciations and where the versions disagree. | `lore.md`: The Myth, Sources, Characters, Words and Phrases | `Researching` |
| 3 | **Shape the album.** Decide the point of view and the arc, then split it into tracks. | `README.md`: Concept, Story Arc, Tracklist. `lore.md`: Track-by-Track Story Map | `Writing` |
| 4 | **Set the sound.** Adjust the mythology's base Suno style prompt for this album. | `README.md` › Sound | `Writing` |
| 5 | **Write each track file,** one per song, with its four parts: the story behind the song (from the sources), the Suno style, the lyrics optimised for Suno (see `lyrics.md` and `suno.md`), and the song's cover art prompt. | `tracks/NN-*.md` §1–4 | `Writing` |
| 6 | **Generate.** Several generations per track. Note the one you keep in the optional log. Extend or replace sections as needed. | `tracks/NN-*.md` › log | `Generating` |
| 7 | **Listen through the album in order.** Check the flow, keys, tempos, the recurring motif and the story. Regenerate any track that breaks the arc. | Notes in `README.md` | `Generating` |
| 8 | **Cover art.** Do the album cover first, then each song's track art from its §4 prompt, in the same visual family. | `art/cover-prompts.md`, the track files §4, and the images | `Art` |
| 9 | **Master and export** (optional external mastering). | Masters kept outside git; lengths go in the tracklist | `Mastering` |
| 10 | **Release.** Descriptions, tags, AI disclosure, links. Update both indexes. | `release/release-notes.md`; status in all READMEs | `Released` |

## Checklist Before Release
- [ ] Every track in the tracklist has a file with all four parts filled in (story, Suno style, Suno lyrics, cover prompt), plus a kept generation and a length.
- [ ] Names in the lyrics match `lore.md` (spelling and pronunciation).
- [ ] `lore.md` lists its sources and says where we took liberties.
- [ ] The Sensitivity section is filled in (or marked "n/a").
- [ ] The cover is 3000×3000 px or larger, with no text or artefacts the platform would reject.
- [ ] The AI disclosure matches the distributor's current rules.
- [ ] The status is updated in the album README, the mythology README and `mythologies/README.md`.
