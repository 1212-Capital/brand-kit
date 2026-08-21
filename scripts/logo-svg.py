#!/usr/bin/env python3
"""Outlines the logotype to SVG from the Lora variable font, matching the Pencil lockups exactly
(1212.pen, Brand Kit frame: "1212" + "CAPITAL", Lora 600, 40px, gap 8, CAPITAL letter-spacing 1).
Usage: python3 scripts/logo-svg.py            (writes Logos/*/ *.svg)
Needs fontTools + brotli (pip install fonttools brotli)."""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "Brand/Fonts/lora-latin-wght-normal.woff2"
WEIGHT = 600
INK, PAPER, LAVENDER, LAVENDER_DEEP = "#1C1A17", "#F2EEE4", "#9B94C7", "#6E6796"

font = instantiateVariableFont(TTFont(FONT), {"wght": WEIGHT})
cmap = font.getBestCmap()
glyphs = font.getGlyphSet()
upm = font["head"].unitsPerEm


def run(text, size, x, spacing=0.0):
    """Glyph paths for `text` at `size`px starting at x, letter-spaced by `spacing`px. Returns (paths, next_x)."""
    out = []
    for i, ch in enumerate(text):
        g = glyphs[cmap[ord(ch)]]
        pen = SVGPathPen(glyphs)
        g.draw(pen)
        bp = BoundsPen(glyphs)
        g.draw(bp)
        out.append((pen.getCommands(), x, bp.bounds))
        x += g.width * size / upm + (spacing if i < len(text) - 1 else 0)
    return out, x


def svg(words, size, colors, out_path):
    """words: list of (text, letter_spacing); one colour per word. Tight viewBox around the ink."""
    scale = size / upm
    items, x = [], 0.0
    for (text, ls), color in zip(words, colors):
        paths, x = run(text, size, x, ls)
        items += [(p, px, b, color) for p, px, b in paths]
        x += 8 * size / 40  # word gap: 8px at 40px
    xs0 = min(px + b[0] * scale for _, px, b, _ in items if b)
    xs1 = max(px + b[2] * scale for _, px, b, _ in items if b)
    ys0 = min(-b[3] * scale for _, _, b, _ in items if b)
    ys1 = max(-b[1] * scale for _, _, b, _ in items if b)
    w, h = xs1 - xs0, ys1 - ys0
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.2f}" height="{h:.2f}" viewBox="{xs0:.3f} {ys0:.3f} {w:.3f} {h:.3f}">']
    parts.append(f"<title>{' '.join(t for t, _ in words)}</title>")
    for d, px, _, color in items:
        parts.append(f'<path fill="{color}" transform="translate({px:.3f} 0) scale({scale:.6f} {-scale:.6f})" d="{d}"/>')
    parts.append("</svg>")
    out_path.write_text("\n".join(parts) + "\n")
    print(out_path.relative_to(ROOT), f"{w:.1f}x{h:.1f}")


svg([("1212", 0), ("CAPITAL", 1)], 40, [INK, LAVENDER], ROOT / "Logos/Horizontal/1212-capital-horizontal.svg")
svg([("1212", 0), ("CAPITAL", 1)], 40, [PAPER, LAVENDER_DEEP], ROOT / "Logos/Reversed/1212-capital-reversed.svg")
svg([("1212", 0)], 55, [INK], ROOT / "Logos/Symbol/1212-symbol.svg")
