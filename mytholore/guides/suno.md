# Suno Guide

Suno changes often (models, character limits, features). **Check the current limits in the app**, and record the model version for every generation, so older tracks can be understood later.

## Style Prompts
- **Build in layers:** genre and subgenre → era or production feel → instruments → vocals → mood → tempo or key (optional).
  ```
  symphonic power metal, epic folk metal, galloping double bass, hurdy-gurdy, tagelharpa, war drums,
  soaring clean male vocals, huge choir chorus, full orchestra, heroic, cinematic, 150 bpm
  ```
- **Keep one base prompt per mythology** (in its README) and **one per album** (in the album README). Track prompts adjust the album prompt. They never start from scratch, so the album stays coherent.
- **Put the most important words first.** Front-load the core genre.
- **Don't name real artists or bands.** Describe the sound instead.
- **Use "exclude styles"** (when available) to keep out things the model drifts toward, for example `pop, EDM, autotune`.

## The Band's Default Exclude List
```
death metal, doom metal, growls, screamed vocals, pop, EDM, autotune
```

## Metatags in Lyrics
Square-bracket tags steer structure and delivery. Suno treats them as hints, not guarantees.
- **Structure:** `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Breakdown]`, `[Interlude]`, `[Outro]`, `[End]`
- **Instrumental sections:** `[Guitar Solo]`, `[Instrumental]`, `[Drum Break]`, `[Orchestral Swell]`
- **Vocal delivery:** `[Powerful Male Vocals]`, `[High Male Vocals]`, `[Deep Male Vocals]`, `[Operatic Female Vocal]`, `[Female Vocal]`, `[Duet]`, `[Choir]`, `[Chant]`, `[Spoken Word]`, `[Whisper]`. Mytholore does **not** use harsh vocals or growls (see the band sound in the main README).
- **Atmosphere or effects** (use sparingly): `[Thunder]`, `[War Horns]`, `[Silence]`
- End with `[End]` to reduce the chance of the song trailing on.

Record in the track file which tags worked and which Suno ignored, so we learn what this band's sound responds to.

## Generating and Choosing
1. Generate several versions per track. Listen for vocal clarity on names, the energy of the chorus, and how the track fits the album's sound.
2. Log every version worth remembering in the track's **Generations** table, with its link or ID and the model. Mark the kept one.
3. **Extend** to add sections or fix endings. **Replace section** to fix one bad line. Note which you used.
4. If a name is mis-sung, respell it phonetically **in the lyrics sent to Suno** (for example `Ragna-rok`, `Yeh-mahn-jah`). Keep the correct spelling in the track file's heading and in `lore.md`.

## Consistency Across an Album
- Keep the same model version for the whole album where possible.
- Reuse the album style prompt word for word, and add at most a few words per track.
- If a recurring motif matters, describe it the same way every time ("the horn call from the intro returns").

## Rights and Disclosure
Check Suno's current terms for your subscription tier (commercial use and ownership), and your distributor's AI-content rules. Record the wording you used in `release/release-notes.md` › AI Disclosure.
