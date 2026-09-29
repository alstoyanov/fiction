# Cover Art Guide

## Band-Wide Identity
Decide these once and apply them to every cover, so Mytholore releases are recognisable in a grid of thumbnails:
- **Logo:** placement (for example top centre) and colour rules.
- **Title typography:** one or two fonts for all album titles.
- **Framing:** for example a central figure or scene, with a dark vignette.

Each **mythology** then sets its own colours, motifs and art style (mythology README › Visual Palette). Each **album** picks one moment from its myth.

## Prompt Format
Write prompts in the same order every time, so they can be compared across models:
```
[subject and moment from the myth], [composition and camera], [art style / medium],
[lighting and colour palette], [mythology-specific motifs], [mood],
[quality terms], [aspect ratio / parameters]
```
Example:
```
Fenrir breaking the chain Gleipnir under a blood-red sky, low-angle wide shot,
dark oil painting in the style of 19th-century romanticism, red and ash-gray palette,
Norse knotwork border, apocalyptic, highly detailed, square format
```

## Per-Model Notes
Keep one short section per tool you use, and update it as you learn what works.
- **<Model 1>:** <what it's good at, parameters that work, known weaknesses (hands, text, symbols)>
- **<Model 2>:**

## What to Check Before Choosing
- **Symbols are correct for the mythology.** AI often mixes cultures: Norse runes on Egyptian scenes, generic "tribal" patterns. Compare against the references in `lore.md`.
- **No garbled text or pseudo-letters** in the image. Add real typography afterwards.
- **Sacred imagery:** respect the mythology README's "Avoid" list, especially for living traditions.
- **Resolution:** 3000×3000 px or larger for streaming. Upscale if needed, and note the upscaler.
- **Artefacts:** extra limbs, melted weapons, mismatched eyes.

## Album Cover and Track Art
- The **album cover** is in `art/cover-prompts.md`, and each **song's art prompt** is §4 of its track file.
- Build the track prompts from the album cover's prompt. Keep the style, medium, palette and framing, and change only the subject: the moment from that song.
- Use the same model and parameters for every track in the album, so the singles look like one set.

## Record Everything
Every kept candidate goes into `art/cover-prompts.md` with its model, prompt, parameters and seed, so a variant (single cover, banner, merch) can be regenerated later in the same style.
