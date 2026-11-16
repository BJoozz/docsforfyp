"""Slides 6-8 of the CA deck: the collaborative design history.

Used two ways:
- build_deck.py calls apply() while building from the GPT draft;
- apply_slides_6_8.py calls apply() on an already finalised deck, so only these
  three slides change and PowerPoint's own parts (videos, timings) stay untouched.
The text comes from slides_6_8_copy.json; the images from ../design-history/,
../early-prototypes/ and Codex's pack.
"""
import json
from pathlib import Path

from PIL import Image
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from pptlib import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
GH = 'https://github.com/BJoozz/docsforfyp/blob/main/'


def _fit(path, x, y, w, h):
    iw, ih = Image.open(path).size
    a = iw / ih
    if w / h > a:
        nw = h * a
        return x + (w - nw) / 2, y, nw, h
    nh = w / a
    return x, y + (h - nh) / 2, w, nh


def _pic(slide, path, x, y, w, h, name):
    fx, fy, fw, fh = _fit(path, x, y, w, h)
    picture(slide, path, fx, fy, fw, fh, name=name)
    return fx, fy, fw, fh


def _outline(slide, x, y, w, h, color, name, lw=2.25):
    box(slide, x, y, w, h, fill=None, line=color, line_w=lw, radius=0.04, name=name)


def _notes(header, script, visual, sources, review=None):
    parts = [header, '', script.strip(), '', 'VISUAL', visual.strip()]
    if review:
        parts += ['', 'TEAM REVIEW', review]
    parts += ['', 'SOURCE'] + sources
    return '\n'.join(parts)


def apply(slides, repo, copy=None):
    """slides: {6: slide, 7: slide, 8: slide}; repo: docsforfyp root (Path)."""
    repo = Path(repo)
    copy = copy or json.loads((HERE / 'slides_6_8_copy.json').read_text(encoding='utf-8'))
    media = repo / 'presentation/ca-2026-11-16-deck-media'
    dh = media / 'design-history'
    ep = media / 'early-prototypes'
    pack = repo / 'presentation/ca-2026-11-16'
    img = {
        'grid': dh / 'A1_wireframes_at_a_glance_v1-v9_crop.png',
        'wf_v2': dh / 'A2_wireframe_v2_split_rails.png',
        'wf_v7': dh / 'A3_wireframe_v7_docks.png',
        'b_v2': dh / 'B1_graph_v2_split_rails.png',
        'b_v7': dh / 'B2_graph_v7_docks.png',
        'bt_v2': dh / 'B3_tree_v2_split_rails.png',
        'bt_v7': dh / 'B4_tree_v7_docks.png',
        'kit_home': dh / 'C1_ui_kit_home.png',
        'kit_viz': dh / 'C2_ui_kit_visualisation.png',
        'p_graph': ep / '03_graph_v2_workspace.png',
        'p_tree': ep / '04_tree_binary_lifting_table_crop.png',
        'p_sort': ep / '05_sorting_two_panes_crop.png',
        'v10': pack / '01_main_slides/04_tree_insert_preview.png',
    }
    missing = [k for k, p in img.items() if not p.exists()]
    if missing:
        raise SystemExit(f'slides 6-8: missing images {missing}')

    # ------------------------------------------------------------------ slide 6
    s, c = slides[6], copy['slide6']
    clear_body(s)
    set_title_text(s, c['title'])
    style_title(s)
    CY, CH = 1.36, 3.92
    cols = [(0.62, c['left_heading'], c['left_points'], [img['p_graph']], '01'),
            (6.77, c['right_heading'], c['right_points'], [img['kit_home'], img['kit_viz']], '02')]
    for k, (x, heading, pts, pics, num) in enumerate(cols):
        box(s, x, CY, 5.95, CH, fill=WHITE, line=BORDER, name=f'card-{k}')
        badge(s, x + 0.22, CY + 0.2, num, name=f'number-{k}')
        who, sep, rest = heading.partition(' · ')
        runs = [(who, {'size': 18, 'color': TEAL}), (sep + rest, {'size': 14.5, 'color': NAVY})] if sep else [(heading, {})]
        text(s, x + 0.82, CY + 0.17, 4.95, 0.52, [runs], size=17, color=NAVY, bold=True,
             anchor=MSO_ANCHOR.MIDDLE, name=f'point-{k}')
        n = len(pics)
        gap = 0.14
        pw = (5.95 - 0.44 - gap * (n - 1)) / n
        for j, pth in enumerate(pics):
            _pic(s, pth, x + 0.22 + j * (pw + gap), CY + 0.85, pw, 1.72, f'image-{k}-{j}')
        text(s, x + 0.22, CY + 2.74, 5.5, 1.12, [[('•  ' + p, {})] for p in pts], size=13.5, color=INK,
             space_after=5, name=f'detail-{k}')
    BY = 5.44
    box(s, 0.62, BY, 12.1, 1.12, fill=TINT, name='bridge')
    text(s, 0.84, BY + 0.1, 6.0, 0.3, c['bridge_label'], size=13, color=TEAL, bold=True, name='bridge-label')
    for k, chip_text in enumerate(c['bridge_chips']):
        chip(s, 0.84 + k * 3.92, BY + 0.47, 3.74, 0.5, chip_text, fill=WHITE, color=NAVY, size=14, line=BORDER,
             name=f'req-{k}')
    text(s, 0.62, 6.68, 12.1, 0.3, c['footer'], size=12, color=MUTED, name='capture-source')
    set_notes(s, _notes(
        'Bao | Early Design | 90 seconds including actions', c['notes_script'],
        'Left card: a still of my standalone Graph rewrite (slide 5 showed all three prototypes). Right card: two screens of '
        'Kerk\'s design-system UI kit, rendered from his first commit of 3 September 2026; they recreate visualgo.net\'s home and '
        'visualisation pages in the new style. The band lists the requirements carried forward.',
        [GH + 'docs/CA_PRESENTATION_CONTRIBUTION_MAP.md', GH + '01_scope_and_timeline.md',
         'Images: ' + GH + 'presentation/ca-2026-11-16-deck-media/design-history/README.md and '
         + GH + 'presentation/ca-2026-11-16-deck-media/early-prototypes/README.md']))

    # ------------------------------------------------------------------ slide 7
    s, c = slides[7], copy['slide7']
    clear_body(s)
    set_title_text(s, c['title'])
    style_title(s)
    TY = 1.36

    def step(x, w, num, heading, detail, k):
        badge(s, x, TY, num, d=0.42, size=12, name=f'number-{k}')
        text(s, x + 0.54, TY - 0.08, w - 0.54, 0.58, heading, size=14.5, color=NAVY, bold=True,
             anchor=MSO_ANCHOR.MIDDLE, name=f'point-{k}')
        text(s, x, TY + 0.6, w, 0.66, detail, size=12.5, color=INK, name=f'detail-{k}')

    IY, IH = 2.68, 2.62
    # step 1: the nine wireframes at a glance, V2 and V7 outlined
    step(0.62, 3.85, '01', c['step1_heading'], c['step1_detail'], 0)
    gx, gy, gw, gh = _pic(s, img['grid'], 0.62, IY, 3.85, IH, 'wireframes')
    for key, colour in (('v2', TEAL), ('v7', TEAL)):
        fx, fy, fw, fh = copy['grid_cells'][key]
        _outline(s, gx + fx * gw, gy + fy * gh, fw * gw, fh * gh, colour, f'pick-{key}')
    text(s, 0.62, IY + IH + 0.06, 3.85, 0.42, c['wireframes_caption'], size=12, color=MUTED, name='cap-wireframes')
    arrow(s, 4.53, IY + IH / 2, 4.81, IY + IH / 2, color=TEAL, name='flow-0')
    # step 2: the two chosen wireframes
    step(4.9, 2.5, '02', c['step2_heading'], c['step2_detail'], 1)
    half = (IH - 0.16) / 2
    for j, (key, label) in enumerate((('wf_v2', 'V2 · split rails'), ('wf_v7', 'V7 · draggable docks'))):
        yy = IY + j * (half + 0.16)
        _pic(s, img[key], 4.9, yy, 2.5, half - 0.24, f'chosen-{j}')
        text(s, 4.9, yy + half - 0.22, 2.5, 0.24, label, size=11, color=INK, bold=True, align=PP_ALIGN.CENTER,
             name=f'chosen-label-{j}')
    arrow(s, 7.46, IY + IH / 2, 7.74, IY + IH / 2, color=TEAL, name='flow-1')
    # step 3: Bao's working builds
    step(7.83, 4.89, '03', c['step3_heading'], c['step3_detail'], 2)
    bw = (4.89 - 0.14) / 2
    for j, (key, label) in enumerate((('b_v2', 'V2 · split rails, working'), ('b_v7', 'V7 · docks, working'))):
        xx = 7.83 + j * (bw + 0.14)
        _pic(s, img[key], xx, IY, bw, IH - 0.3, f'build-{j}')
        text(s, xx, IY + IH - 0.26, bw, 0.24, label, size=11, color=INK, bold=True, align=PP_ALIGN.CENTER,
             name=f'build-label-{j}')
    text(s, 7.83, IY + IH + 0.06, 4.89, 0.42, c['builds_caption'], size=12, color=MUTED, name='cap-builds')
    card(s, 0.62, 5.92, 12.1, 0.72, c['band'], fill=TINT, size=14, color=NAVY, anchor=MSO_ANCHOR.MIDDLE, pad=0.2,
         name='band')
    set_notes(s, _notes(
        'Kerk | UI/UX Evolution | 90 seconds including actions', c['notes_script'],
        'Left: Kerk\'s wireframe page of 4 September 2026, its "At a glance" grid of nine frames with V2 and V7 outlined. '
        'Middle: the V2 and V7 wireframes. Right: Bao\'s working Graph builds in V2 (split rails) and V7 (docks). He made them on '
        '20 to 27 September; the stills show them as they stood on 17 October, at the last commit that still had them (ae63a62).',
        [GH + '03_architecture_and_decisions.md', GH + '01_scope_and_timeline.md',
         'Images: ' + GH + 'presentation/ca-2026-11-16-deck-media/design-history/README.md'],
        review='Kerk to confirm this slide: the wireframes, the student feedback he organised and the wording of the choice.'))

    # ------------------------------------------------------------------ slide 8
    s, c = slides[8], copy['slide8']
    clear_body(s)
    set_title_text(s, c['title'])
    style_title(s)
    LY = 1.36
    for k, (heading, pts, key) in enumerate(((c['from_v2_heading'], c['from_v2_points'], 'bt_v2'),
                                              (c['from_v7_heading'], c['from_v7_points'], 'bt_v7'))):
        y = LY + k * 1.9
        box(s, 0.62, y, 4.25, 1.76, fill=WHITE, line=BORDER, name=f'from-{k}')
        _pic(s, img[key], 0.78, y + 0.16, 1.55, 0.97, f'from-image-{k}')
        text(s, 2.48, y + 0.12, 2.3, 0.5, heading, size=13.5, color=TEAL, bold=True, name=f'from-heading-{k}')
        tb = text(s, 2.48, y + 0.68, 2.3, 1.0, [[('•  ' + p, {})] for p in pts], size=12.5, color=INK, space_after=3,
                  name=f'from-points-{k}')
        for para in tb.text_frame.paragraphs:  # hanging indent: wrapped lines start under the text
            ppr = para._p.get_or_add_pPr()
            ppr.set('marL', '152400')
            ppr.set('indent', '-152400')
    arrow(s, 4.95, LY + 1.83, 5.32, LY + 1.83, color=TEAL, width=2.5, name='join')
    # V10: the current app with its regions outlined
    VX, VW = 5.42, 4.7
    vx, vy, vw, vh = _pic(s, img['v10'], VX, LY, VW, 3.66, 'v10')
    sc = vw / 1440
    for (px, py, pw, ph, colour, name) in ((2, 42, 298, 794, TEAL, 'r-left'), (306, 42, 808, 794, NAVY, 'r-canvas'),
                                           (1120, 42, 318, 794, TEAL, 'r-right'), (2, 842, 1436, 56, MUTED, 'r-footer')):
        box(s, vx + px * sc, vy + py * sc, pw * sc, ph * sc, fill=None, line=colour, line_w=2, radius=0.02, name=name)
    text(s, 10.3, LY - 0.02, 2.42, 0.4, c['v10_heading'], size=15.5, color=NAVY, bold=True, name='v10-heading')
    for k, (pt, colour) in enumerate(zip(c['v10_points'], (NAVY, TEAL, MUTED))):
        y = LY + 0.55 + k * 1.02
        box(s, 10.3, y + 0.07, 0.16, 0.16, fill=colour, shape=MSO_SHAPE.OVAL, name=f'swatch-{k}')
        text(s, 10.56, y - 0.03, 2.16, 0.95, pt, size=14, color=NAVY, bold=True, name=f'point-{k}')
    CYB = 5.28
    box(s, 0.62, CYB, 12.1, 1.3, fill=TINT, name='credit')
    for k, line in enumerate(c['credit_lines']):
        head, _, rest = line.partition(': ')
        runs = [(head + (': ' if rest else ''), {'bold': True, 'color': NAVY}), (rest, {})] if rest else [(line, {})]
        text(s, 0.84, CYB + 0.12 + k * 0.37, 11.7, 0.34, [runs], size=13.5, color=INK, name=f'credit-{k}')
    text(s, 0.62, 6.68, 12.1, 0.3, c['footer'], size=12, color=MUTED, name='capture-source')
    set_notes(s, _notes(
        'Kerk | UI/UX Evolution | 90 seconds including actions', c['notes_script'],
        'Left: Bao\'s working Tree builds in V2 (split rails) and V7 (docks), as of 17 October, with what V10 keeps from each. '
        'Right: the current app (Tree Editor, app 346e84b) with coloured outlines for the tab groups, the canvas and the shared '
        'playback bar; the three points beside it use the same colours.',
        [GH + '03_architecture_and_decisions.md', GH + '01_scope_and_timeline.md',
         'Images: ' + GH + 'presentation/ca-2026-11-16-deck-media/design-history/README.md; current app: '
         + GH + 'presentation/ca-2026-11-16/01_main_slides/04_tree_insert_preview.png'],
        review='Kerk to confirm this slide: his refinements, the consolidation and how the decision is described.'))
    return ['6 two parallel foundations', '7 nine wireframes to two working prototypes', '8 V2 and V7 to V10']
