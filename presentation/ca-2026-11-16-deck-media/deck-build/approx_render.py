"""Approximate slide renderer for layout checks when PowerPoint cannot be automated.

It draws the shapes this deck uses (rectangles, rounded rectangles, ovals, text
boxes, pictures, straight connectors) with Pillow and Arial metrics. It is NOT
PowerPoint: use it only to catch overflow, overlap and misplaced blocks, and
render with PowerPoint (render.ps1) before trusting fine detail.

    py -3.12 approx_render.py deck.pptx outdir 6,7,8
"""
import io
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.enum.dml import MSO_FILL
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

DPI = 120
EMU = 914400
FONTS = 'C:/Windows/Fonts/'


def px(emu):
    return int(round(emu / EMU * DPI))


def font(size_pt, bold):
    return ImageFont.truetype(FONTS + ('arialbd.ttf' if bold else 'arial.ttf'), max(6, int(round(size_pt * DPI / 72))))


def solid(fill):
    try:
        if fill.type == MSO_FILL.SOLID:
            return '#' + str(fill.fore_color.rgb)
    except Exception:
        pass
    return None


def draw_text(d, shape, x, y, w, h, report):
    tf = shape.text_frame
    ml, mr, mt, mb = px(tf.margin_left), px(tf.margin_right), px(tf.margin_top), px(tf.margin_bottom)
    bw = max(10, w - ml - mr)
    lines = []  # (list of (text, font, colour), height, align, space_after)
    for p in tf.paragraphs:
        runs = [(r.text, r.font.size.pt if r.font.size else 14, bool(r.font.bold),
                 '#' + str(r.font.color.rgb) if r.font.color and r.font.color.type is not None else '#24394B')
                for r in p.runs if r.text]
        if not runs:
            lines.append(([], int(14 * DPI / 72 * 1.2), p.alignment, 0))
            continue
        words = []
        for text, size, bold, colour in runs:
            f = font(size, bold)
            parts = text.split(' ')
            for i, part in enumerate(parts):
                words.append((part + (' ' if i < len(parts) - 1 else ''), f, colour, size))
        cur, cur_w = [], 0
        para_lines = []
        for word, f, colour, size in words:
            ww = d.textlength(word, font=f)
            if cur and cur_w + d.textlength(word.rstrip(), font=f) > bw:
                para_lines.append(cur)
                cur, cur_w = [], 0
            cur.append((word, f, colour, size))
            cur_w += ww
        if cur:
            para_lines.append(cur)
        sa = int((p.space_after.pt if p.space_after is not None else 0) * DPI / 72)
        for i, ln in enumerate(para_lines):
            hmax = max(s for _, _, _, s in ln)
            lines.append(([(t, f, c) for t, f, c, _ in ln], int(hmax * DPI / 72 * 1.2), p.alignment,
                          sa if i == len(para_lines) - 1 else 0))
    total = sum(lh + sa for _, lh, _, sa in lines)
    inner_h = h - mt - mb
    if tf.vertical_anchor == MSO_ANCHOR.MIDDLE:
        cy = y + mt + (inner_h - total) / 2
    elif tf.vertical_anchor == MSO_ANCHOR.BOTTOM:
        cy = y + mt + inner_h - total
    else:
        cy = y + mt
    if total > inner_h + 4 and shape.text_frame.text.strip():
        report.append(f'OVERFLOW {shape.name!r}: text {total}px in {inner_h}px box: {shape.text_frame.text[:50]!r}')
    for runs, lh, align, sa in lines:
        lw = sum(d.textlength(t, font=f) for t, f, _ in runs)
        if align == PP_ALIGN.CENTER:
            cx = x + ml + (bw - lw) / 2
        elif align == PP_ALIGN.RIGHT:
            cx = x + ml + bw - lw
        else:
            cx = x + ml
        for t, f, c in runs:
            d.text((cx, cy), t, font=f, fill=c)
            cx += d.textlength(t, font=f)
        cy += lh + sa


def render(slide, bg='#FAFBFD'):
    W, H = int(13.333 * DPI), int(7.5 * DPI)
    try:
        if slide.background.fill.type == MSO_FILL.SOLID:
            bg = '#' + str(slide.background.fill.fore_color.rgb)
    except Exception:
        pass
    im = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(im)
    report = []
    for sh in slide.shapes:
        x, y, w, h = px(sh.left), px(sh.top), px(sh.width), px(sh.height)
        if x + w > W + 2 or y + h > H + 2 or x < -2 or y < -2:
            report.append(f'OFF-SLIDE {sh.name!r}')
        if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
            pic = Image.open(io.BytesIO(sh.image.blob)).convert('RGB').resize((max(1, w), max(1, h)), Image.LANCZOS)
            im.paste(pic, (x, y))
            d.rectangle([x, y, x + w, y + h], outline='#CFDAE3')
            continue
        if sh.shape_type == MSO_SHAPE_TYPE.LINE or sh.shape_type == MSO_SHAPE_TYPE.FREEFORM or not hasattr(sh, 'text_frame'):
            try:
                d.line([px(sh.begin_x), px(sh.begin_y), px(sh.end_x), px(sh.end_y)], fill='#087F8C', width=2)
            except Exception:
                pass
            continue
        fill = solid(sh.fill)
        line = None
        try:
            if sh.line.fill.type == MSO_FILL.SOLID:
                line = '#' + str(sh.line.color.rgb)
        except Exception:
            line = None
        lw = max(1, int(round((sh.line.width.pt if line and sh.line.width else 1) * DPI / 72))) if line else 0
        kind = None
        try:
            kind = str(sh.auto_shape_type)
        except Exception:
            pass
        if fill or line:
            if kind and 'OVAL' in kind:
                d.ellipse([x, y, x + w, y + h], fill=fill, outline=line, width=lw or 1)
            elif kind and 'ROUNDED' in kind:
                try:
                    r = int(min(w, h) * sh.adjustments[0])
                except Exception:
                    r = 6
                d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=line, width=lw or 1)
            else:
                d.rectangle([x, y, x + w, y + h], fill=fill, outline=line, width=lw or 1)
        if sh.has_text_frame and sh.text_frame.text:
            draw_text(d, sh, x, y, w, h, report)
    return im, report


if __name__ == '__main__':
    deck, outdir = sys.argv[1], Path(sys.argv[2])
    wanted = [int(n) for n in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
    outdir.mkdir(parents=True, exist_ok=True)
    prs = Presentation(deck)
    for i, s in enumerate(prs.slides, 1):
        if wanted and i not in wanted:
            continue
        im, rep = render(s)
        im.save(outdir / f'approx-{i:02d}.png')
        print(f'slide {i}: {len(rep)} warnings')
        for r in rep:
            print('  ', r)
