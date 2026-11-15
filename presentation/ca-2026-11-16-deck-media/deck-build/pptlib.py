"""Small helpers for editing the CA deck with python-pptx (Arial, deck palette)."""
from copy import deepcopy
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree

NAVY = '142B43'
TEAL = '087F8C'
INK = '24394B'
MUTED = '637587'
LTEAL = 'BDE9E9'
BG = 'FAFBFD'
CARD = 'EEF3F7'
TINT = 'E3F2F3'
BORDER = 'CFDAE3'
WHITE = 'FFFFFF'
GREEN = '1E7B4E'
GREEN_TINT = 'E2F3EA'
AMBER = '9A5B00'
AMBER_TINT = 'FCEFD8'
FONT = 'Arial'


def rgb(hexstr):
    return RGBColor.from_string(hexstr)


def I(v):
    return Inches(v)


def remove_shape(shape):
    el = shape._element
    el.getparent().remove(el)


def clear_body(slide, keep=('title', 'page')):
    for sh in list(slide.shapes):
        if sh.name not in keep:
            remove_shape(sh)


def shape_by_name(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    return None


def _style_runs(paragraph, size, color, bold, italic=False):
    for r in paragraph.runs:
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = rgb(color)


def set_text(tf, parts, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, margin=0.0, space_after=0, line_spacing=None):
    """parts: str, or list of paragraphs; a paragraph is str or list of
    (text, {size,color,bold,italic}) runs."""
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = anchor
    m = I(margin)
    tf.margin_left = tf.margin_right = m
    tf.margin_top = tf.margin_bottom = m
    paras = parts if isinstance(parts, list) else [parts]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if space_after:
            p.space_after = Pt(space_after)
        if line_spacing:
            p.line_spacing = line_spacing
        runs = para if isinstance(para, list) else [(para, {})]
        for text, fmt in runs:
            r = p.add_run()
            r.text = text
            r.font.name = FONT
            r.font.size = Pt(fmt.get('size', size))
            r.font.bold = fmt.get('bold', bold)
            r.font.italic = fmt.get('italic', False)
            r.font.color.rgb = rgb(fmt.get('color', color))
    return tf


def text(slide, x, y, w, h, parts, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, name=None, space_after=0, line_spacing=None, margin=0.0):
    tb = slide.shapes.add_textbox(I(x), I(y), I(w), I(h))
    if name:
        tb.name = name
    set_text(tb.text_frame, parts, size, color, bold, align, anchor, margin, space_after, line_spacing)
    return tb


def box(slide, x, y, w, h, fill=CARD, line=None, line_w=0.75, radius=0.06, name=None,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE, dash=False):
    sp = slide.shapes.add_shape(shape, I(x), I(y), I(w), I(h))
    if name:
        sp.name = name
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sp.adjustments[0] = radius
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid()
        sp.fill.fore_color.rgb = rgb(fill)
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = rgb(line)
        sp.line.width = Pt(line_w)
        if dash:
            ln = sp.line._get_or_add_ln()
            d = etree.SubElement(ln, qn('a:prstDash'))
            d.set('val', 'dash')
    # no theme shadow / effects
    style = sp._element.find(qn('p:style'))
    if style is not None:
        sp._element.remove(style)
    sp.text_frame.text = ''
    return sp


def card(slide, x, y, w, h, parts, fill=CARD, line=None, size=15, color=INK, bold=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, pad=0.18, name=None, radius=0.06,
         dash=False, space_after=0, line_spacing=None):
    sp = box(slide, x, y, w, h, fill=fill, line=line, radius=radius, name=name, dash=dash)
    set_text(sp.text_frame, parts, size, color, bold, align, anchor, pad, space_after, line_spacing)
    return sp


def badge(slide, x, y, label, d=0.46, fill=TEAL, color=WHITE, size=13, name=None):
    sp = box(slide, x, y, d, d, fill=fill, shape=MSO_SHAPE.OVAL, name=name)
    set_text(sp.text_frame, label, size, color, True, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE, 0.0)
    return sp


def chip(slide, x, y, w, h, label, fill=TINT, color=TEAL, size=12, bold=True, name=None, line=None):
    sp = box(slide, x, y, w, h, fill=fill, line=line, radius=0.5, name=name)
    set_text(sp.text_frame, label, size, color, bold, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE, 0.04)
    return sp


def arrow(slide, x1, y1, x2, y2, color=MUTED, width=1.75, name=None, dash=False, head=True):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
    if name:
        c.name = name
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(width)
    ln = c.line._get_or_add_ln()
    if dash:
        d = etree.SubElement(ln, qn('a:prstDash'))
        d.set('val', 'dash')
    if head:
        t = etree.SubElement(ln, qn('a:tailEnd'))
        t.set('type', 'triangle')
        t.set('w', 'med')
        t.set('len', 'med')
    style = c._element.find(qn('p:style'))
    if style is not None:
        c._element.remove(style)
    return c


def picture(slide, path, x, y, w=None, h=None, border=BORDER, name=None):
    pic = slide.shapes.add_picture(str(path), I(x), I(y), I(w) if w else None, I(h) if h else None)
    if name:
        pic.name = name
    if border:
        pic.line.color.rgb = rgb(border)
        pic.line.width = Pt(0.75)
    return pic


def movie(slide, mp4, poster, x, y, w, h, name=None, border=BORDER):
    mv = slide.shapes.add_movie(str(mp4), I(x), I(y), I(w), I(h),
                                poster_frame_image=str(poster), mime_type='video/mp4')
    if name:
        mv.name = name
    if border:
        mv.line.color.rgb = rgb(border)
        mv.line.width = Pt(0.75)
    return mv


def set_notes(slide, body):
    tf = slide.notes_slide.notes_text_frame
    tf.text = body.strip('\n')


def style_title(slide, size=32, top=0.34, height=0.82, color=NAVY):
    t = shape_by_name(slide, 'title')
    if t is None:
        return None
    t.left, t.top, t.width, t.height = I(0.62), I(top), I(12.1), I(height)
    tf = t.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for p in tf.paragraphs:
        for r in p.runs:
            r.font.size = Pt(size)
            r.font.color.rgb = rgb(color)
            r.font.bold = True
            r.font.name = FONT
    return t


def set_title_text(slide, new_text):
    t = shape_by_name(slide, 'title')
    p = t.text_frame.paragraphs[0]
    runs = p.runs
    runs[0].text = new_text
    for r in runs[1:]:
        r.text = ''
