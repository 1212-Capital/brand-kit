# 1212 Capital — Brand Kit

The brand assets and design system for 1212 Capital. Everything here is the
current, approved version. When something looks different elsewhere, this wins.

1212 Capital is a crypto-native family office. The identity is warm and
editorial rather than fintech-cold: painterly golden-hour landscapes, a serif
voice, and a calm palette that stays clear while the market is loud.

> **Anchored in traditional finance. Fluent in digital asset markets.**

## Contents

| Folder | What's in it |
|---|---|
| **Logos/** | The logotype: horizontal, symbol, and reversed for dark backgrounds. SVG and PNG. |
| **Illustrations/** | The 18 painted landscapes, in three sets by time of day. Full-resolution masters, plus web-sized copies. |
| **Templates/** | Social canvases: announcement, stat, split, editorial and story formats in 16:9, 1:1 and 9:16. |
| **Brand/** | Colour, typography and the fonts themselves. |
| **Documents/** | What a fact sheet, newsletter, internal document and client statement look like, as reference PDFs. |

`1212 Brand Assets.zip` at the root holds the full-resolution masters in one
download, for anyone who doesn't want to clone the repository.

## Logos

| File | Use |
|---|---|
| `Logos/Horizontal/` | The default lockup, `1212` in ink and `CAPITAL` in lavender. |
| `Logos/Symbol/` | `1212` alone, when the space is too tight for the full lockup or the context already says who we are. |
| `Logos/Reversed/` | The lockup on dusk and other dark surfaces. |

| `Logos/Avatars/` | Square profile pictures for LinkedIn, X and anywhere else that crops to a circle. |

The SVGs carry outlined paths, so they render identically without the font
installed. Give the logotype room to breathe, and never redraw, restyle,
recolour or stretch it.

### Avatars

Three backgrounds, ivory, dusk and lavender, each at 1024, 512 and 400 px.
Use 400 for a LinkedIn or X profile picture, 512 for a favicon or app icon,
1024 when something asks for the largest version.

The mark is `1212` alone, never the full lockup: `CAPITAL` becomes unreadable
at avatar sizes and gets clipped by the circular crop. The mark occupies just
over half the square, which keeps it clear of that crop on every platform.

## Illustrations

Three sets of six, named for the light rather than the place:

- **Dawn** — cool lilac light, 06:00
- **Noon** — bright blue, 12:12
- **Dusk** — warm orange, 18:00

Masters are full-resolution PNG, 16:9. `Illustrations/Web/` holds the same
images at 1600×900 as JPEG, which is what documents and web pages should use.

Every full-bleed placement needs a scrim so light type stays legible. The
document scrim is a five-stop gradient:

```
linear-gradient(180deg, #201C2B8C 0%, #201C2B1A 24%, #201C2B26 44%, #201C2BD9 72%, #201C2BFC 100%)
```

Recheck contrast whenever the image changes. Never generate a new brand image:
use the library.

## Colour

| Token | Hex | Role |
|---|---|---|
| ivory | `#FBF8EF` | page background, light panels |
| paper | `#F2EEE4` | cards, tables, tiles |
| sand | `#F2E8D5` | working surfaces only, never a published page |
| ink | `#1C1A17` | primary text |
| ink-soft | `#6F685C` | secondary text, labels |
| line | `#D9D2C3` | every rule and hairline, 1px |
| terracotta | `#B05A3C` | data, highlight |
| lavender | `#9B94C7` | the wordmark CAPITAL, primary data colour |
| lilac | `#D8D2E6` | section tags, highlighted rows |
| periwinkle | `#CDD6EC` | pills, data |
| amber | `#EBA23A` | data |
| gold-sun | `#F2CE97` | data |
| dusk | `#262233` | data bands, dark surfaces |
| mint | `#D6EACF` | pastel tag |
| peach | `#F3DAC8` | pastel tag |

Text on a pastel uses the matching tint, never ink: lilac `#4A4370`, mint
`#2E4A2A`, peach `#6E3B26`, periwinkle `#3A4166`.

Data always follows one ramp, in this order: **lavender → gold-sun →
terracotta → periwinkle → amber**. Warm accents belong to data and highlights;
they do not decorate.

## Typography

| Family | Role |
|---|---|
| **Lora** | Display only, weight 500. 600 appears in the logotype and nowhere else. |
| **Inter** | Body copy, labels, tables, UI. |
| **IBM Plex Mono** | Eyebrows, meta lines, and every figure in a document. |

A number set in Lora or Inter inside a document is a bug. All three families
are free under the SIL Open Font License; copies and the licence are in
`Brand/Fonts/`.

## The rules that get broken most

- Radii are 999 for tags and pills, 10 for surfaces, 24 on social canvases,
  6 for buttons, 0 for everything else.
- Every hairline is `line` at 1px. No black rules, no heavier weights.
- `vermilion`, `teal`, `accent-blue` and `paper-2` are not brand colours, even
  though they still exist as variables in the design file.
- No em dashes in copy. Use a period or a comma.
- On an inner page of a document, an image must carry information. The
  landscapes are the cover's job.

## Documents

`Documents/` holds a reference PDF of each of the four document templates, in
their blank state: fact sheet, newsletter, internal document, client statement.
They are there to be looked at, so you can see the system applied to a page
without installing anything.

They are **not** the editable templates, on purpose. A copy of a template
here would drift from the real one within a month. The editable versions live
in exactly two places:

- **Pencil**, in `1212.pen`, for anyone maintaining the design.
- **The Claude plugin**, `1212-Capital/claude-plugins`, which builds the PDFs
  from this same system without Pencil.

Ask Claude for "the monthly fact sheet" or "this month's newsletter" with the
plugin installed, and it produces the real thing.

Note the difference from the social canvases in `Templates/`: those are
finished images you post as they are. Documents are generated from data.

## Licence

Copyright © 2026 1212 Capital Inc. All rights reserved. See `LICENSE`.
