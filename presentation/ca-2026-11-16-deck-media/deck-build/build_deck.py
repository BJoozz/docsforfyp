"""Build the improved CA deck from the GPT draft.

Run from the docsforfyp repository root (needs python-pptx, lxml and Pillow):
    py -3.12 presentation/ca-2026-11-16-deck-media/deck-build/build_deck.py \
        presentation/drafts/VisuAlgo_CA_Presentation_MediaLinked_GPT_draft.pptx out.pptx
then let PowerPoint add the click-to-play effects (finalize.ps1, see README.md).
Media come from presentation/ca-2026-11-16 (Codex pack), presentation/ca-2026-11-16-deck-media
(new captures) and figures/ (historical 1 Nov captures). Crops are written to
presentation/ca-2026-11-16-deck-media/deck-crops/.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from PIL import Image
from pptx import Presentation
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptlib import *  # noqa

DRAFT, OUT = Path(sys.argv[1]), Path(sys.argv[2])
REPO = Path('.').resolve()
PACK = REPO / 'presentation/ca-2026-11-16'
NEW = REPO / 'presentation/ca-2026-11-16-deck-media'
CROPS = NEW / 'deck-crops'
CROPS.mkdir(parents=True, exist_ok=True)
FIG = REPO / 'figures'
GH = 'https://github.com/BJoozz/docsforfyp/blob/main/'
LCA_VARIANT = '01b_lca_keep_then_jump'  # or '01_lca_equal_ancestors'


def first(*paths):
    for p in paths:
        if p and Path(p).exists():
            return Path(p)
    return None


def crop(src, box_px, name):
    out = CROPS / name
    Image.open(src).convert('RGB').crop(box_px).save(out, optimize=True)
    return out


def aspect(path):
    w, h = Image.open(path).size
    return w / h


def fit(path, x, y, w, h):
    """Return (x, y, w, h) that fits the image inside the box, centred."""
    a = aspect(path)
    if w / h > a:
        nw = h * a
        return x + (w - nw) / 2, y, nw, h
    nh = w / a
    return x, y + (h - nh) / 2, w, nh


def clip(slug):
    mp4 = NEW / 'clips' / f'{slug}.mp4'
    poster = NEW / 'posters' / f'{slug}.png'
    return (mp4, poster) if mp4.exists() and poster.exists() else (None, None)


prs = Presentation(str(DRAFT))
S = {i + 1: s for i, s in enumerate(prs.slides)}
LOG = []

# ---------- common: titles in one place and size on every content slide ----------
for i, s in S.items():
    if i in (1, 23):
        continue
    style_title(s)

MEDIA_X, MEDIA_Y, MEDIA_W, MEDIA_H = 4.0, 1.36, 8.72, 5.45
CAP_Y = 6.86


def caption(slide, words, x=MEDIA_X, w=MEDIA_W):
    text(slide, x, CAP_Y, w, 0.28, words, size=12, color=MUTED, name='capture-source')


def points(slide, items, x=0.62, y=1.5, w=3.15, pitch=1.62, head=17, sub=12.5, num=True):
    """items: list of (heading, sub) -> numbered blocks at a fixed pitch; heading and
    detail share one text box so PowerPoint flows them."""
    for k, (h1, h2) in enumerate(items):
        cy = y + k * pitch
        if num:
            text(slide, x, cy, 0.5, 0.35, f'{k + 1:02d}', size=14, color=TEAL, bold=True, name=f'number-{k}')
        hx = x + (0.5 if num else 0)
        hw = w - (0.5 if num else 0)
        paras = [[(h1, {'bold': True, 'color': NAVY, 'size': head})]]
        if h2:
            paras.append([(h2, {'size': sub, 'color': MUTED})])
        text(slide, hx, cy - 0.03, hw, pitch - 0.1, paras, name=f'point-{k}', space_after=4)
    return y + len(items) * pitch


def media_slide(slide, still=None, mp4=None, poster=None, cap='', name='media'):
    if mp4 is not None:
        movie(slide, mp4, poster, MEDIA_X, MEDIA_Y, MEDIA_W, MEDIA_H, name=name)
    elif still is not None:
        x, y, w, h = fit(still, MEDIA_X, MEDIA_Y, MEDIA_W, MEDIA_H)
        picture(slide, still, x, y, w, h, name=name)
    caption(slide, cap)


def notes_get(slide):
    return slide.notes_slide.notes_text_frame.text


def notes_replace(slide, old, new):
    t = notes_get(slide)
    if old not in t:
        raise SystemExit(f'notes text not found on slide: {old[:60]!r}')
    set_notes(slide, t.replace(old, new))


# ======================= slide 1: title =======================
s = S[1]
hero_src = first(NEW / 'posters' / f'{LCA_VARIANT}.png', PACK / '01_main_slides/02_dijkstra_decision.png')
hero = crop(PACK / '01_main_slides/02_dijkstra_decision.png', (300, 40, 1440, 900), 'title_hero.png')
for nm, (x, y, w, h) in {'title': (0.81, 1.62, 6.1, 1.1), 'subtitle': (0.85, 2.85, 5.9, 1.25),
                          'presenters': (0.85, 4.55, 6.0, 0.95)}.items():
    sh = shape_by_name(s, nm)
    sh.left, sh.top, sh.width, sh.height = I(x), I(y), I(w), I(h)
text(s, 0.85, 5.62, 6.0, 0.6, ['NUS School of Computing · CP4101 Continuous Assessment', '16 November 2026'],
     size=13, color='9FB3C6', name='event')
hx, hy, hw, hh = fit(hero, 7.15, 1.3, 5.6, 4.9)
picture(s, hero, hx, hy, hw, hh, border='3A5571', name='hero')
text(s, hx, hy + hh + 0.08, hw, 0.28, 'VisuAlgo+ prototype',
     size=10.5, color='9FB3C6', name='hero-caption')

# ======================= slide 2: motivation =======================
s = S[2]
clear_body(s)
c1 = crop(PACK / '01_main_slides/06_v10_layout.png', (330, 75, 1090, 550), 'mot_graph.png')
c2 = crop(PACK / '01_main_slides/02_dijkstra_decision.png', (520, 195, 1110, 564), 'mot_canvas.png')
c3 = crop(PACK / '01_main_slides/05_sorting_compare.png', (0, 85, 1152, 805), 'mot_sorting.png')
TRIE_STILL = NEW / 'stills' / 'trie_insert_care_frame5.png'
c4 = crop(TRIE_STILL, (326, 120, 1094, 730), 'trie_insert.png')
cards = [
    ('More convenient graph editing', 'Draw and change the graph you are studying, with parallel and curved edges handled clearly', c1),
    ('Richer interaction on the canvas', 'Inspect a step, move things and see why a decision happens', c2),
    ('Sorting comparison on the same input', 'Several algorithms on one dataset, side by side', c3),
    ('A wider range of algorithms', 'More topics, such as LCA with Binary Lifting and Trie, on foundations that make later ones easier to add', c4),
]
for k, (h1, h2, img) in enumerate(cards):
    x = 0.62 + k * 3.08
    box(s, x, 1.42, 2.86, 5.12, fill=WHITE, line=BORDER, name=f'card-{k}')
    badge(s, x + 0.2, 1.6, f'{k + 1:02d}', name=f'number-{k}')
    text(s, x + 0.2, 2.18, 2.46, 0.72, h1, size=17, color=NAVY, bold=True, name=f'point-{k}')
    text(s, x + 0.2, 2.98, 2.46, 1.35, h2, size=13.5, color=INK, name=f'detail-{k}')
    ix, iy, iw, ih = fit(img, x + 0.2, 4.5, 2.46, 1.54)
    picture(s, img, ix, iy, iw, ih, name=f'image-{k}')
text(s, 0.62, 6.72, 11.6, 0.3,
     'Directions proposed by Prof. Halim in early weekly meetings · images: the VisuAlgo+ prototype',
     size=12, color=MUTED, name='capture-source')
notes_replace(s, 'Editing, playback and comparison were goals from the beginning. The prototypes helped us investigate how to implement them.',
              'He also encouraged us to widen the range of algorithms that VisuAlgo+ can visualize, so we wanted foundations that make '
              'new topics easier to add. These were goals from the beginning, and the prototypes helped us investigate how to reach them.')

# ======================= slide 3: why rebuild =======================
s = S[3]
clear_body(s)
text(s, 0.62, 1.45, 6.0, 0.3, 'Original VisuAlgo graph topics (simplified)', size=13, color=MUTED, bold=True, name='diagram-label')
for k, topic in enumerate(['Traversal', 'Shortest paths', 'Spanning trees']):
    x = 0.62 + k * 2.0
    card(s, x, 1.85, 1.85, 1.55, [[(topic, {'bold': True, 'size': 15, 'color': NAVY})],
                                  [('own input handling', {'size': 12.5, 'color': INK})],
                                  [('own state building', {'size': 12.5, 'color': INK})]],
         fill=WHITE, line=BORDER, pad=0.14, space_after=3, name=f'topic-{k}')
    arrow(s, x + 0.925, 3.42, x + 0.925, 4.12, name=f'arrow-{k}')
card(s, 0.62, 4.15, 5.85, 0.72, 'Shared graph widget (drawing)', fill=TINT, size=15, color=TEAL, bold=True,
     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name='shared-widget')
card(s, 0.62, 5.15, 5.85, 0.95, 'One editing change → coordinated changes and checks across every topic',
     fill=AMBER_TINT, size=14.5, color=AMBER, bold=True, anchor=MSO_ANCHOR.MIDDLE, name='consequence')
for k, (h1, h2) in enumerate([
        ('Shared components already exist', 'for example, a graph widget used by several topics'),
        ('Module-specific logic complicates common changes', 'input handling and visual-state building live inside each topic'),
        ('New interactions need clearer state boundaries', 'comparison panes need their own state but shared controls')]):
    y = 1.8 + k * 1.5
    text(s, 7.05, y, 0.6, 0.4, f'{k + 1:02d}', size=18, color=TEAL, bold=True, name=f'number-{k}')
    text(s, 7.7, y - 0.04, 5.0, 1.4, [[(h1, {'bold': True, 'color': NAVY, 'size': 19})],
                                      [(h2, {'size': 13.5, 'color': MUTED})]], space_after=4, name=f'point-{k}')

# ======================= slide 4: objectives =======================
s = S[4]
clear_body(s)
objs = [
    ('A reusable visualization and interaction layer',
     'Graph, Tree and Sorting share one V10 shell; LCA and Trie already run on it',
     'Stabilize the shown workflows; add topics on the same foundations'),
    ('A renewed website and execution foundation',
     'Site with catalogue and routes; a separate C++/WebAssembly engine foundation',
     'Connect the engine and infrastructure to the visualizers'),
    ('A working prototype with further integration ahead',
     'Students tried the V10 prototype in Week 10', 'Validate, then an initial release around March 2027 (target)'),
]
for k, (h1, now, nxt) in enumerate(objs):
    x = 0.62 + k * 4.2
    box(s, x, 1.42, 3.7, 4.45, fill=WHITE, line=BORDER, name=f'card-{k}')
    badge(s, x + 0.25, 1.64, f'{k + 1:02d}', name=f'number-{k}')
    text(s, x + 0.85, 1.58, 2.7, 1.0, h1, size=18, color=NAVY, bold=True, anchor=MSO_ANCHOR.MIDDLE, name=f'point-{k}')
    chip(s, x + 0.25, 2.85, 0.85, 0.34, 'NOW', fill=GREEN_TINT, color=GREEN, size=11, name=f'now-chip-{k}')
    text(s, x + 0.25, 3.27, 3.2, 1.1, now, size=14.5, color=INK, name=f'now-{k}')
    chip(s, x + 0.25, 4.45, 0.85, 0.34, 'NEXT', fill=AMBER_TINT, color=AMBER, size=11, name=f'next-chip-{k}')
    text(s, x + 0.25, 4.87, 3.2, 0.9, nxt, size=14.5, color=INK, name=f'next-{k}')
card(s, 0.62, 6.08, 12.1, 0.72,
     [[('Current boundary: ', {'bold': True, 'color': NAVY}),
       ('the visualizers run TypeScript algorithms in the browser. The engine is a separate foundation; '
        'connecting it is Semester 2 work.', {})]],
     fill=TINT, size=14.5, anchor=MSO_ANCHOR.MIDDLE, name='boundary')

notes_replace(S[4], 'build clearer boundaries for future development, and validate the resulting functionality.',
              'build clearer boundaries so that new algorithms are easier to add, and validate the resulting functionality.')
LOG.append('1-4 restyled')

# ======================= slide 5: early prototypes =======================
s = S[5]
EP = NEW / 'early-prototypes'
ep_imgs = {k: first(*(sorted(EP.glob(pat)) if EP.exists() else [])) for k, pat in {
    'g1edit': '01_graph_v1_edit*.png', 'g1run': '02_graph_v1_run*.png', 'g2': '03_graph_v2*.png',
    'tree': '04_tree*.png', 'sort': '05_sorting*.png'}.items()}
EP_RUN, EP_V2 = EP / '02_graph_v1_run_crop.png', EP / '03_graph_v2_workspace.png'
EP_TREE, EP_SORT = EP / '04_tree_binary_lifting_table_crop.png', EP / '05_sorting_two_panes_crop.png'
EARLY_READY = all(p.exists() for p in (EP_RUN, EP_V2, EP_TREE, EP_SORT))
if EARLY_READY:
    clear_body(s)
    heads = [(0.62, 5.0, 'Graph: editing and playback on one canvas'),
             (5.92, 3.3, 'Tree: structural operations and ancestor information'),
             (9.52, 3.2, 'Sorting: independent runs with shared controls')]
    for k, (x, w, h1) in enumerate(heads):
        text(s, x, 1.38, 0.5, 0.4, f'{k + 1:02d}', size=15, color=TEAL, bold=True, name=f'number-{k}')
        text(s, x + 0.5, 1.38, w - 0.5, 0.8, h1, size=15, color=NAVY, bold=True, name=f'point-{k}')
    # Graph: prototype 1 run view -> rewrite with one canvas
    gx, gy = 0.62, 2.3
    x, y, w, h = fit(EP_RUN, gx, gy, 2.25, 2.3)
    picture(s, EP_RUN, x, y, w, h, name='graph-v1')
    text(s, gx, gy + 2.38, 2.25, 0.5, 'Prototype 1 (Aug): a separate run view with Back to Edit', size=11, color=MUTED, name='cap-v1')
    arrow(s, gx + 2.3, gy + 1.15, gx + 2.62, gy + 1.15, color=TEAL, name='g-arrow')
    x, y, w, h = fit(EP_V2, gx + 2.68, gy, 2.32, 2.3)
    picture(s, EP_V2, x, y, w, h, name='graph-v2')
    text(s, gx + 2.68, gy + 2.38, 2.32, 0.5, 'Rewrite (Sep): one canvas for editing and playback', size=11, color=MUTED, name='cap-v2')
    x, y, w, h = fit(EP_TREE, 5.92, 2.3, 3.3, 2.3)
    picture(s, EP_TREE, x, y, w, h, name='tree')
    text(s, 5.92, 4.68, 3.3, 0.5, 'Tree prototype (Sep): Binary Lifting builds its ancestor table', size=11, color=MUTED, name='cap-tree')
    x, y, w, h = fit(EP_SORT, 9.52, 2.3, 3.2, 2.3)
    picture(s, EP_SORT, x, y, w, h, name='sorting')
    text(s, 9.52, 4.68, 3.2, 0.5, 'Sorting Room (Aug): two panes on one input, shared controls', size=11, color=MUTED, name='cap-sort')
    for k, (x, w, t) in enumerate([(0.62, 5.0, 'Moving a vertex keeps the same step; input, positions and playback are separate'),
                                   (5.92, 3.3, 'LCA: an ancestor table beside the tree · Trie: insert and search along a prefix · changes previewed before Apply'),
                                   (9.52, 3.2, 'Each pane keeps its own state; one transport moves them together')]):
        card(s, x, 5.3, w, 1.25, t, fill=TINT, size=13, anchor=MSO_ANCHOR.MIDDLE, pad=0.16, name=f'tested-{k}')
    text(s, 0.62, 6.66, 12.1, 0.3, 'Standalone prototypes, built July to September 2026', size=12, color=MUTED, name='capture-source')
    notes_replace(s, 'For Tree, I explored operations that change the structure, and how to inspect a proposed result before applying it. '
                  'Binary Lifting also required a tree and an ancestor table to explain one query together.',
                  'The Tree prototype also widened the range of topics: it included LCA with Binary Lifting, and Trie. '
                  'Different algorithms brought different visualization needs: an ancestor table beside the tree for LCA queries, '
                  'and insert and search along a prefix for Trie. For operations that change the structure, I explored how to '
                  'inspect a proposed result before applying it.')
    notes_replace(s, 'SOURCE\n', 'VISUAL\nPoint left to right: the dark prototype-1 run view (it has its own Back to Edit button), '
                  'the rewrite with one canvas, the Tree prototype with its ancestor table, and Sorting Room with two panes. '
                  'These are the old standalone builds, rebuilt from their last documented commits and captured on 16 November 2026, '
                  'not the current app. The Tree prototype also had a Trie workspace (Insert and Search), which is not pictured.\n\nSOURCE\n')
    notes_replace(s, 'CA_PRESENTATION_PROTOTYPE_REVIEW.md',
                  'CA_PRESENTATION_PROTOTYPE_REVIEW.md\n'
                  f'Stills: {GH}presentation/ca-2026-11-16-deck-media/early-prototypes/README.md (manifest.json lists repo, ref and commit date per image)')
    LOG.append('5 early prototypes placed')
else:
    LOG.append('5 left as draft (no early-prototype stills yet)')

# ======================= slides 6-8: the design history =======================
# Slide 6 (Bao): two parallel foundations. Slide 7 (Kerk): nine wireframes to two
# working prototypes. Slide 8 (Kerk): V2 and V7 to V10. Layout in slides_6_8.py,
# text in slides_6_8_copy.json, images in ../design-history/.
import slides_6_8
LOG.extend(slides_6_8.apply({6: S[6], 7: S[7], 8: S[8]}, REPO))

# ======================= slide 9: application boundaries (Kerk) =======================
s = S[9]
clear_body(s)
card(s, 0.62, 1.45, 8.9, 0.8, [[('01  ', {'color': LTEAL}), ('Site host', {'bold': True}), ('  ·  routes, top bar and theme', {})]],
     fill=NAVY, size=17, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, pad=0.25, name='site-host')
text(s, 0.62, 2.45, 8.9, 0.4, [[('02  ', {'color': TEAL}), ('Visualizers: input, execution and playback', {})]],
     size=16, color=NAVY, bold=True, name='point-1')
for k, (vz, tech) in enumerate([('Graph', 'React Flow drawing · D3 layout'), ('Tree', 'React Flow drawing · D3 layout'),
                                ('Sorting', 'Canvas 2D arrays')]):
    x = 0.62 + k * 3.0
    card(s, x, 2.92, 2.9, 1.45, [[(vz, {'bold': True, 'size': 17, 'color': NAVY})],
                                 [('TypeScript in the page', {'size': 13, 'color': TEAL, 'bold': True})],
                                 [(tech, {'size': 12, 'color': MUTED})]],
         fill=WHITE, line=BORDER, pad=0.18, space_after=3, name=f'viz-{k}')
card(s, 0.62, 4.57, 8.9, 0.8, [[('03  ', {'color': TEAL}), ('Shared layer', {'bold': True, 'color': NAVY}),
                               ('  ·  layout and presentation utilities', {})]],
     fill=TINT, size=17, anchor=MSO_ANCHOR.MIDDLE, pad=0.25, name='shared-layer')
card(s, 9.9, 1.45, 2.82, 3.92, [[('04', {'color': AMBER, 'bold': True, 'size': 15})],
                                [('Separate engine foundation awaiting integration', {'bold': True, 'color': NAVY, 'size': 17})],
                                [('C++ compiled to WebAssembly; a separate project today', {'size': 13.5})]],
     fill=WHITE, line=AMBER, dash=True, pad=0.22, space_after=8, name='engine')
arrow(s, 9.55, 3.65, 9.88, 3.65, color=AMBER, dash=True, name='to-engine')
text(s, 0.62, 5.65, 12.1, 0.7, 'One React and TypeScript application built with Vite. The shell knows where a panel sits; '
     'the algorithm decides what that panel means.', size=14, color=MUTED, name='footnote')

# ======================= slide 10: engine foundation (Kerk) =======================
s = S[10]
clear_body(s)
card(s, 0.62, 1.75, 3.3, 2.9, [[('Page', {'bold': True, 'size': 20, 'color': NAVY})],
                               [('interaction and drawing', {'size': 15})],
                               [('interprets engine state for the learner', {'size': 13.5, 'color': MUTED})]],
     fill=WHITE, line=BORDER, pad=0.25, space_after=6, anchor=MSO_ANCHOR.MIDDLE, name='page-box')
card(s, 4.55, 2.45, 3.2, 1.5, [[('03  ', {'color': TEAL}), ('Protocol messages connect the page and engine', {'bold': True, 'color': NAVY})],
                               [('protobuf · graph and array representations', {'size': 12.5, 'color': MUTED})]],
     fill=TINT, size=15, anchor=MSO_ANCHOR.MIDDLE, pad=0.18, space_after=4, name='protocol')
arrow(s, 3.95, 2.95, 4.52, 2.95, color=TEAL, name='p-to-m')
arrow(s, 4.52, 3.45, 3.95, 3.45, color=TEAL, name='m-to-p')
arrow(s, 7.78, 2.95, 8.35, 2.95, color=TEAL, name='m-to-w')
arrow(s, 8.35, 3.45, 7.78, 3.45, color=TEAL, name='w-to-m')
box(s, 8.38, 1.45, 4.34, 3.5, fill=CARD, line=BORDER, name='worker')
text(s, 8.6, 1.58, 3.9, 0.4, [[('02  ', {'color': TEAL}), ('Execution inside a worker', {})]], size=16, color=NAVY, bold=True, name='worker-label')
card(s, 8.6, 2.15, 3.9, 1.2, [[('01  ', {'color': TEAL}), ('C++20 compiled to WebAssembly', {'bold': True, 'color': NAVY})],
                              [('the algorithm engine', {'size': 13, 'color': MUTED})]],
     fill=WHITE, line=BORDER, size=15.5, anchor=MSO_ANCHOR.MIDDLE, pad=0.18, space_after=3, name='wasm')
card(s, 8.6, 3.5, 3.9, 1.25, [[('04  ', {'color': TEAL}), ('Python tracing explored through Pyodide', {'bold': True, 'color': NAVY})],
                              [('for sorting algorithms', {'size': 13, 'color': MUTED})]],
     fill=WHITE, line=BORDER, size=15.5, anchor=MSO_ANCHOR.MIDDLE, pad=0.18, space_after=3, name='pyodide')
card(s, 0.62, 5.3, 12.1, 1.3,
     [[('Design question: ', {'bold': True, 'color': NAVY}),
       ('expose enough algorithm state for visualization without making the engine depend on the page layout. '
        'A distance update alone does not decide where a note appears or which pseudocode line to emphasise.', {})]],
     fill=TINT, size=15, anchor=MSO_ANCHOR.MIDDLE, pad=0.25, name='question')

# ======================= slide 11: reversible execution (Kerk) =======================
s = S[11]
clear_body(s)
card(s, 0.62, 1.45, 5.7, 2.3, [[('01  ', {'color': TEAL}), ('Engine history', {'bold': True, 'color': NAVY})],
                               [('A reversible journal of records for every step; moving backward replays those records.', {'size': 15})]],
     fill=WHITE, line=BORDER, size=19, pad=0.25, space_after=6, name='engine-history')
card(s, 7.02, 1.45, 5.7, 2.3, [[('02  ', {'color': TEAL}), ('Current visualizers', {'bold': True, 'color': NAVY})],
                               [('Graph and Tree build a step sequence when a run starts.', {'size': 15})],
                               [('Sorting pulls generator operations and keeps history for seeking.', {'size': 15})]],
     fill=WHITE, line=BORDER, size=19, pad=0.25, space_after=6, name='viz-history')
chip(s, 6.38, 2.35, 0.58, 0.5, '≠', fill=AMBER_TINT, color=AMBER, size=20, name='neq')
arrow(s, 6.67, 3.85, 6.67, 4.35, color=TEAL, name='down')
box(s, 0.62, 4.45, 12.1, 1.75, fill=TINT, name='preserve')
text(s, 0.87, 4.6, 11.6, 0.4, [[('03  ', {'color': TEAL}), ('Integration must preserve identity and step meaning', {})]],
     size=18, color=NAVY, bold=True, name='point-2')
for k, c in enumerate(['Node and edge identity (parallel edges)', 'The same run across edits and restarts',
                       'State, pseudocode and notes agree on a step']):
    chip(s, 0.87 + k * 3.92, 5.3, 3.75, 0.62, c, fill=WHITE, color=NAVY, size=13.5, line=BORDER, name=f'keep-{k}')

# ======================= slide 12: website integration (Kerk) =======================
s = S[12]
clear_body(s)
box(s, 0.62, 1.45, 8.4, 4.6, fill=WHITE, line=BORDER, radius=0.03, name='browser')
box(s, 0.62, 1.45, 8.4, 0.85, fill=NAVY, radius=0.03, name='browser-bar')
text(s, 0.87, 1.5, 8.0, 0.75, [[('01  ', {'color': LTEAL}), ('One site controls navigation and theme', {'bold': True})]],
     size=17, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, name='point-0')
for k, (vz, ctl) in enumerate([('Graph', 'algorithm choice'), ('Tree', 'operation and query'), ('Sorting', 'pane controls')]):
    x = 0.9 + k * 2.75
    card(s, x, 2.6, 2.5, 1.55, [[(vz, {'bold': True, 'size': 17, 'color': NAVY})],
                                [('supplies ' + ctl, {'size': 13})]],
         fill=CARD, pad=0.18, space_after=4, name=f'slot-{k}')
text(s, 0.9, 4.35, 7.9, 0.75, [[('02  ', {'color': TEAL, 'bold': True}),
                                ('Visualizers supply topic-specific controls; the host presents them in one site, '
                                 'with no second set of playback controls.', {})]],
     size=14.5, color=INK, name='point-1')
card(s, 9.3, 1.45, 3.42, 4.6, [[('03', {'color': TEAL, 'bold': True, 'size': 15})],
                               [('Shared infrastructure supports further integration', {'bold': True, 'color': NAVY, 'size': 17})],
                               [('website infrastructure and the engine still need to meet the visualization layer', {'size': 13.5})]],
     fill=TINT, pad=0.25, space_after=8, name='infra')
text(s, 0.62, 6.3, 12.1, 0.35, 'Bao: functional catalogue, routes and host adapters on the design system · Kerk: consolidation and refinements',
     size=12.5, color=MUTED, name='attribution')

LOG.append('8-12 restyled (Kerk to confirm content)')

# ======================= slide 13: my contributions =======================
s = S[13]
clear_body(s)
contrib = [
    ('Graph, Tree and Sorting foundations', 'Graph rewrite keeps document, layout, session and presentation apart; Tree operations; Sorting Room'),
    ('Algorithm and operation extensions', 'more topics: LCA (Binary Lifting), Trie, recursive DFS, Bellman-Ford, Prim, bridges, AVL, heap, lazy segment tree; each with its own steps, pseudocode and inspector'),
    ('V10 shell and site integration', 'tab groups, drag, split and resize, validated saved layouts; catalogue, routes, host adapters'),
    ('Step explanations and validation', 'floating text, paused focus, final recap; independent oracles, property and regression tests'),
]
thumbs13 = [
    crop(PACK / '01_main_slides/03_dijkstra_final_path_t.png', (400, 230, 1060, 642), 'c13_graph.png'),
    c4,
    crop(PACK / '01_main_slides/06_v10_layout.png', (300, 300, 1120, 812), 'c13_shell.png'),
    crop(PACK / '01_main_slides/02_dijkstra_decision.png', (560, 205, 880, 405), 'c13_note.png'),
]
for k, (h1, h2) in enumerate(contrib):
    x = 0.62 + (k % 2) * 6.15
    y = 1.45 + (k // 2) * 2.62
    box(s, x, y, 5.95, 2.42, fill=WHITE, line=BORDER, name=f'card-{k}')
    badge(s, x + 0.25, y + 0.25, f'{k + 1:02d}', name=f'number-{k}')
    text(s, x + 0.85, y + 0.2, 4.9, 0.6, h1, size=19, color=NAVY, bold=True, anchor=MSO_ANCHOR.MIDDLE, name=f'point-{k}')
    text(s, x + 0.25, y + 0.95, 3.35, 1.4, h2, size=13.5 if k == 1 else 14.5, color=INK, name=f'detail-{k}')
    tx, ty, tw, th = fit(thumbs13[k], x + 3.75, y + 0.95, 1.98, 1.24)
    picture(s, thumbs13[k], tx, ty, tw, th, name=f'thumb-{k}')
text(s, 0.62, 6.75, 12.1, 0.3, 'Selected decisions follow',
     size=12, color=MUTED, name='capture-source')

notes_replace(S[13], 'My contribution covers the visualizer foundations, algorithm execution and operation extensions, the V10 shell, and integration into the site. '
              'I also worked on how individual steps communicate their meaning and how the behavior is tested. I will show selected decisions across these areas.',
              'My contribution covers the visualizer foundations, the V10 shell and integration into the site. It also covers the algorithms themselves: '
              'I added topics such as LCA with Binary Lifting and Trie, and each algorithm needs its own step model, pseudocode and inspector. '
              'I also worked on how individual steps communicate their meaning and how the behavior is tested. I will show selected decisions.')
LOG.append('13 restyled')

# ======================= slides 14-18 & 24: media =======================
NEW_CAP = 'Real app capture'

# 14 V10 shell
s = S[14]
clear_body(s)
V10_CLIP = '02b_v10_split_left_bottom' if clip('02b_v10_split_left_bottom')[0] else '02_v10_move_panel'
points(s, [('The canvas stays mounted', 'moving Status does not reload the drawing or the run'),
           ('One model governs sizes and valid drops', 'split, join or dock: the preview uses the same geometry as the result'
            if V10_CLIP.startswith('02b') else 'the drop preview uses the same geometry as the result'),
           ('Saved layouts recover safely', 'versioned and checked, repaired or reset')])
mp4, poster = clip(V10_CLIP)
media_slide(s, still=PACK / '01_main_slides/06_v10_layout.png', mp4=mp4, poster=poster,
            cap=NEW_CAP)

# 15 graph state ownership
s = S[15]
clear_body(s)
PAR_DETAIL = 'its own identity and weight: 5 and 2'
G_CLIP = '03b_graph_drag_edit_parallel' if clip('03b_graph_drag_edit_parallel')[0] else '03_graph_drag_then_edit'
PAR = G_CLIP.startswith('03b')
text(s, 0.62, 1.4 if PAR else 1.42, 3.2, 0.3, 'Who owns which state', size=13, color=MUTED, bold=True, name='diagram-label')
owners = [('Document', 'nodes, edges, weights'), ('Layout', 'positions'), ('Session', 'run and selected step'),
          ('Presentation', 'derived highlights' if PAR else 'highlights derived from the step')]
oy, opitch, oh = (1.72, 0.56, 0.5) if PAR else (1.78, 0.72, 0.62)
for k, (o, d) in enumerate(owners):
    card(s, 0.62, oy + k * opitch, 3.15, oh, [[(o, {'bold': True, 'color': NAVY}), ('  ' + d, {'size': 12.5, 'color': INK})]],
         fill=WHITE, line=BORDER, size=14.5, anchor=MSO_ANCHOR.MIDDLE, pad=0.14, name=f'owner-{k}')
outcomes = [('Move a vertex: preserve the run', 'changes Layout only', GREEN_TINT, GREEN),
            ('Change an edge weight: invalidate the run', 'changes the Document', AMBER_TINT, AMBER)]
if PAR:
    outcomes.append(('Add a parallel edge: a separate edge', PAR_DETAIL, TINT, TEAL))
cy, cpitch = (4.06, 0.92) if PAR else (4.82, 0.98)
for k, (h1, h2, fill, ink) in enumerate(outcomes):
    card(s, 0.62, cy + k * cpitch, 3.15, 0.86, [[(h1, {'bold': True})], [(h2, {'size': 12.5})]],
         fill=fill, size=14 if PAR else 14.5, color=ink, anchor=MSO_ANCHOR.MIDDLE, pad=0.14, name=f'point-{k}')
mp4, poster = clip(G_CLIP)
if mp4 is None:
    mp4, poster = PACK / '02_short_clips/01_graph_paused_step.mp4', PACK / '01_main_slides/02_dijkstra_decision.png'
media_slide(s, mp4=mp4, poster=poster, cap=NEW_CAP)

# 16 LCA (shown as slide 17 after the swap at the end of this script)
s = S[16]
clear_body(s)
LCA_CLIP = '01d_lca_reroot_on_camera_8_20'
mp4, poster = clip(LCA_CLIP)
if mp4 is None:
    raise SystemExit(f'LCA clip {LCA_CLIP} is missing')
# what floating text is for, in one card
card(s, 0.62, 1.36, 3.15, 1.02,
     [[('Floating text puts the reason beside the node', {'bold': True, 'color': NAVY, 'size': 14.5})],
      [('9 of this query’s 12 steps carry a note; no node ever moves', {'size': 12, 'color': INK})]],
     fill=TINT, anchor=MSO_ANCHOR.MIDDLE, pad=0.14, space_after=3, name='point-0')
text(s, 0.62, 2.48, 3.15, 0.5,
     [[('Query: LCA(8, 20) = 16', {'bold': True, 'color': NAVY, 'size': 14})],
      [('Balanced · 10 nodes; root moved 10 → 16', {'size': 12, 'color': MUTED})]], space_after=1, name='point-1')
STILLS = NEW / 'stills'
notes3 = [('lca_8_20_depth_lift.png', (430, 578, 870, 711), 'Depth gap 2: lift u from 8 to 4'),
          ('lca_8_20_keep.png', (395, 66, 835, 199), 'Same ancestor 16: keep u and v'),
          ('lca_8_20_lift_both.png', (384, 212, 824, 345), 'Ancestors 10 and 18 differ: lift both')]
for k, (fname, box_px, label) in enumerate(notes3):
    y = 3.1 + k * 1.24
    cimg = crop(STILLS / fname, box_px, 'lca_note_' + fname)
    picture(s, cimg, 0.62, y, 3.15, 3.15 * (box_px[3] - box_px[1]) / (box_px[2] - box_px[0]), name=f'note-{k}')
    text(s, 0.62, y + 0.97, 3.15, 0.24, label, size=11.5, color=INK, bold=True, name=f'note-label-{k}')
media_slide(s, mp4=mp4, poster=poster, cap=NEW_CAP)

# 17 sorting
s = S[17]
clear_body(s)
points(s, [('The same dataset in every pane', '12 values · Bubble and Selection'),
           ('One clock, independent operation streams', 'both panes pause at operation 48'),
           ('Retained history supports seeking', 'the clip ends with Last, a seek to the final operation')], pitch=1.5)
chip(s, 0.62, 6.2, 3.15, 0.5, 'Operation counts are not CPU time', fill=AMBER_TINT, color=AMBER, size=12.5, name='not-cpu')
media_slide(s, mp4=PACK / '02_short_clips/02_sorting_shared_clock.mp4', poster=PACK / '01_main_slides/05_sorting_compare.png',
            cap=NEW_CAP)

# 18 pause and inspect
s = S[18]
clear_body(s)
DIJ_CLIP = '04b_dijkstra_big_note_pause_hover' if clip('04b_dijkstra_big_note_pause_hover')[0] else '04_dijkstra_note_pause_hover'
if DIJ_CLIP.startswith('04b'):
    points(s, [('Paused motion keeps the current relationship visible', 'the counter stays at frame 17 while edge 2 → 3 is emphasised'),
               ('A short note explains the step on arrival', 'frame 18: 12 + 14 < 33 · update'),
               ('Final Dijkstra hover reveals a computed path', '8: 0 → 2 → 3 → 8, distance 42 · 4: distance 46')], head=16)
else:
    points(s, [('Paused motion keeps the current relationship visible', 'the frame counter stays at 11'),
               ('A short note explains the step on arrival', 'frame 12: 1 + 1 < 4 · update'),
               ('Final Dijkstra hover reveals a computed path', 'T: distance 4 · A: distance 2, no rerun')], head=16)
mp4, poster = clip(DIJ_CLIP)
media_slide(s, still=PACK / '01_main_slides/03_dijkstra_final_path_t.png', mp4=mp4, poster=poster,
            cap=NEW_CAP)

# ======================= slide 19: editors =======================
s = S[19]
clear_body(s)
ed = PACK / '01_main_slides/01_editor_entry_points.png'
x, y, w, h = fit(ed, 0.62, 1.4, 12.1, 1.95)
picture(s, ed, x, y, w, h, name='editors')
steps = [('Begin with a graph or tree', 'Graph Editor, or Tree Editor (LCA, BST, AVL)'),
         ('Try compatible algorithms on the example', 'e.g. Dijkstra, then recursive DFS on the same graph'),
         ('Build small tests and investigate conjectures', 'check an observation or look for a counterexample')]
for k, (h1, h2) in enumerate(steps):
    x = 0.62 + k * 4.2
    box(s, x, 3.75, 3.7, 2.2, fill=WHITE, line=BORDER, name=f'card-{k}')
    badge(s, x + 0.25, 3.97, f'{k + 1:02d}', name=f'number-{k}')
    text(s, x + 0.85, 3.9, 2.7, 0.85, h1, size=17, color=NAVY, bold=True, anchor=MSO_ANCHOR.MIDDLE, name=f'point-{k}')
    text(s, x + 0.25, 4.9, 3.2, 0.9, h2, size=14, color=INK, name=f'detail-{k}')
    if k < 2:
        arrow(s, x + 3.72, 4.85, x + 4.18, 4.85, color=TEAL, name=f'flow-{k}')
text(s, 0.62, 6.2, 12.1, 0.55, 'The original VisuAlgo already supports custom input; this is a clearer entry point and workflow. '
     'An intended use, not a measured adoption result.', size=13, color=MUTED, name='limits')
caption(s, NEW_CAP, x=0.62, w=12.1)
notes_replace(s, 'Screenshot: https://github.com/BJoozz/docsforfyp/blob/main/figures/F1-home-catalogue.png\n'
                 'Historical app commit 662e7b3. See figures/README.md for capture details.\n',
              'Historical full home page: https://github.com/BJoozz/docsforfyp/blob/main/figures/F1-home-catalogue.png (662e7b3).\n')

# ======================= slide 20: live demo =======================
# Bao's choice of 16 November: the slide only announces a short demo; what the demo
# shows is settled in the script, not on the slide.
s = S[20]
clear_body(s)
s.background.fill.solid()
s.background.fill.fore_color.rgb = rgb(NAVY)
set_title_text(s, 'Live demo')
t20 = shape_by_name(s, 'title')
t20.left, t20.top, t20.width, t20.height = I(0.83), I(2.19), I(11.46), I(1.04)
for r20 in t20.text_frame.paragraphs[0].runs:
    r20.font.size = Pt(57)
    r20.font.color.rgb = rgb(WHITE)
text(s, 0.88, 3.73, 11.25, 0.9, 'A short demo of VisuAlgo+', size=24, color=LTEAL, name='closing')
for r20 in shape_by_name(s, 'page').text_frame.paragraphs[0].runs:
    r20.font.color.rgb = rgb(LTEAL)

# ======================= slide 21: evaluation =======================
s = S[21]
clear_body(s)
for k, (num, lab) in enumerate([('3,273', 'unit tests passing'), ('151', 'Chromium browser cases')]):
    x = 0.62 + k * 3.0
    box(s, x, 1.45, 2.8, 2.0, fill=WHITE, line=BORDER, name=f'stat-{k}')
    text(s, x + 0.2, 1.55, 2.4, 1.0, num, size=44, color=TEAL, bold=True, name=f'stat-num-{k}')
    text(s, x + 0.2, 2.6, 2.4, 0.6, lab, size=15, color=INK, name=f'stat-lab-{k}')
text(s, 0.62, 3.55, 5.8, 0.6, [[('01  ', {'color': TEAL, 'bold': True}),
                                ('Snapshot of 1 Nov 2026, not a rerun today', {})]],
     size=13.5, color=MUTED, name='point-0')
card(s, 6.85, 1.45, 5.87, 2.0, [[('02  ', {'color': TEAL}), ('Week 10 trial', {'bold': True, 'color': NAVY})],
                                [('NUS students with varied experience used V10 on their own for 15–20 minutes, '
                                  'then a short post-use test and feedback.', {'size': 14.5})]],
     fill=WHITE, line=BORDER, size=18, pad=0.22, space_after=4, name='trial')
card(s, 0.62, 4.3, 12.1, 1.15, [[('03  ', {'color': TEAL}), ('Frequent Status reading motivated floating text', {'bold': True, 'color': NAVY})],
                                [('Design response: short notes near the canvas object, with legend and Status changes '
                                  '(a formative observation, not a coded analysis).', {'size': 14})]],
     fill=TINT, size=18, anchor=MSO_ANCHOR.MIDDLE, pad=0.25, name='response')
card(s, 0.62, 5.65, 12.1, 0.95, [[('04  ', {'color': AMBER}), ('Learning impact remains unmeasured', {'bold': True}),
                                  ('  ·  a follow-up needs defined tasks and the revised interface', {'size': 14, 'bold': False})]],
     fill=AMBER_TINT, size=18, color=AMBER, anchor=MSO_ANCHOR.MIDDLE, pad=0.25, name='limit')

# ======================= slide 22: semester 2 =======================
s = S[22]
clear_body(s)
road = [('Integrate one Graph algorithm end to end', 'input, engine and playback agree on identity, step meaning and cancellation'),
        ('Validate interaction, correctness and resource use', 'startup, seeking and memory on longer runs'),
        ('Evaluate revised explanations with defined tasks', 'e.g. explain why an LCA step keeps both nodes'),
        ('Target an initial release around March 2027', 'original VisuAlgo stays; completed topics are linked')]
for k, (h1, h2) in enumerate(road):
    x = 0.62 + k * 3.06
    box(s, x, 2.05, 2.86, 3.6, fill=TINT if k == 3 else WHITE, line=BORDER, name=f'card-{k}')
    badge(s, x + 0.22, 1.58, f'{k + 1:02d}', d=0.62, size=15, name=f'number-{k}')
    text(s, x + 0.22, 2.4, 2.45, 1.4, h1, size=17.5, color=NAVY, bold=True, name=f'point-{k}')
    text(s, x + 0.22, 3.85, 2.45, 1.6, h2, size=14, color=INK, name=f'detail-{k}')
    if k < 3:
        arrow(s, x + 0.9, 1.89, x + 3.24, 1.89, color=BORDER, width=2, head=False, name=f'line-{k}')
text(s, 0.62, 5.9, 12.1, 0.75, ['March 2027 is a target that depends on integration and validation; '
     'covering the full original algorithm range is the longer-term aim.',
     'Possible later extensions, not Semester 2 commitments: advanced tree topics such as Heavy-Light Decomposition and Centroid Decomposition.'],
     size=13, color=MUTED, name='limits', space_after=3)
notes_replace(s, 'Our broader ambition is to cover the original algorithm range.',
              'Our broader ambition is to cover the original algorithm range and, later, to add advanced topics. For example, the rooted-tree and '
              'ancestor-query work behind LCA could support Heavy-Light Decomposition or Centroid Decomposition. Those are possibilities, not '
              'Semester 2 commitments; integration, validation and stability come first.')

# ======================= slide 23: questions =======================
s = S[23]
text(s, 0.88, 5.6, 11.0, 0.4, 'Evidence and media: github.com/BJoozz/docsforfyp', size=15, color='9FB3C6', name='evidence-link')

# ======================= slide 24: backup BST =======================
s = S[24]
clear_body(s)
points(s, [('Inspect intermediate structures', 'BST Insert(5): the new node is a preview'),
           ('Step backward through the preview', 'the committed tree is unchanged'),
           ('Apply the completed result to the input', 'the tree text gains the edge 6 5')])
mp4, poster = clip('05_bst_preview_apply')
media_slide(s, still=PACK / '01_main_slides/04_tree_insert_preview.png', mp4=mp4, poster=poster,
            cap=NEW_CAP)

# ======================= slide 25: backup correctness =======================
s = S[25]
clear_body(s)
points(s, [('Independent oracle for cut vertices and bridges', 'remove each candidate, recount components'),
           ('Stable edge identity for parallel edges', 'removing one of two parallel edges differs'),
           ('Long sorting histories still cost memory', 'retained history is not bounded')], head=16)
media_slide(s, still=FIG / 'F8-cut-vertex-bridge-cp4-4-7-last.png', cap='Real app capture, 1 Nov 2026')

# ======================= slide 26: backup evidence =======================
s = S[26]
clear_body(s)
ev = [('CA report and architecture records', 'report/main.tex · 03_architecture_and_decisions.md'),
      ('Contribution map and prototype history', 'docs/CA_PRESENTATION_CONTRIBUTION_MAP.md · docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md'),
      ('Week 10 trial addendum', 'report/week10_user_trial_addendum.md'),
      ('Source links in each slide’s notes', 'media manifests: presentation/ca-2026-11-16/ and presentation/ca-2026-11-16-deck-media/')]
for k, (h1, h2) in enumerate(ev):
    x = 0.62 + (k % 2) * 6.15
    y = 1.45 + (k // 2) * 2.35
    box(s, x, y, 5.95, 2.15, fill=WHITE, line=BORDER, name=f'card-{k}')
    badge(s, x + 0.25, y + 0.25, f'{k + 1:02d}', name=f'number-{k}')
    text(s, x + 0.85, y + 0.2, 4.9, 0.6, h1, size=18, color=NAVY, bold=True, anchor=MSO_ANCHOR.MIDDLE, name=f'point-{k}')
    text(s, x + 0.25, y + 0.95, 5.45, 1.0, h2, size=13, color=MUTED, name=f'detail-{k}')
text(s, 0.62, 6.35, 12.1, 0.35, 'Repository: github.com/BJoozz/docsforfyp · application: kerktaiheng/visualgo-plus-design (main 346e84b)',
     size=13, color=MUTED, name='repo')

GH = 'https://github.com/BJoozz/docsforfyp/blob/main/'

set_notes(S[24], f"""Bao | Backup | Q&A / backup

A mutating operation needs a different contract from a read-only query such as LCA. BST Insert(5) runs as a preview: the search path and the new node are visible, and I can step backward through the preview, but the tree document and its text input stay unchanged. Only Apply commits the completed result; the tree text then gains the edge 6 5 and the run ends. Switching to another operation discards the preview. Heap insertion follows the same contract, with an array view alongside the tree.

{{CLIP24}}

SOURCE
{GH}docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md
Historical Heap still: {GH}figures/F6-heap-insert-climb-note.png (app 662e7b3, 1 Nov 2026)""")

set_notes(S[26], f"""Both | Backup | Q&A / backup

Primary evidence lives in BJoozz/docsforfyp: report/main.tex, 03_architecture_and_decisions.md, docs/CA_PRESENTATION_CONTRIBUTION_MAP.md, docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md and report/week10_user_trial_addendum.md. Prototype history: BJoozz/graph-algorithm-visualizer, graph-visualizer-v2, tree-visualizer and sorting-algorithm-visualizer. Application: kerktaiheng/visualgo-plus-design (fork BJoozz/visualgo-plus-design), main 346e84b.

Media in this deck: slides 1, 2, 8, 14-19 and 24 use real captures of app 346e84b from 15-16 November 2026, with manifests and reproduce steps in presentation/ca-2026-11-16/ (Codex pack) and presentation/ca-2026-11-16-deck-media/. Slide 25 uses a historical capture of app 662e7b3 from 1 November 2026, documented in figures/README.md. {{EARLY26}}Slides 6 to 8 use design-history artifacts rendered from their own commits (presentation/ca-2026-11-16-deck-media/design-history/): Kerk's UI kit (634b5be, 3 September) and wireframes (69aa8e4, 4 September), and Bao's working V2 and V7 builds (ae63a62).

The November 16 clarifications record early supervisor direction, the LCA selection and Bao's recollection about Status reading. They also record Bao's account that Prof. Halim encouraged widening the range of algorithms in general (no written record; he did not name specific topics). LCA with Binary Lifting and Trie were built in the standalone Tree prototype in September 2026 and are in the current app. Heavy-Light Decomposition and Centroid Decomposition are possible later extensions and are not implemented. Kerk should review slides 7-12 against his current engine and website work before the joint presentation.

SOURCE
{GH}docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md
{GH}presentation/CA_PRESENTATION_MEDIA_USAGE.md""")

# ======================= slide 27: backup DFS recap (demo fallback) =======================
import copy
mp4, poster = clip('06_dfs_recursive_recap')
if mp4 is not None:
    s27 = prs.slides.add_slide(prs.slide_layouts[5])
    s27.background.fill.solid()
    s27.background.fill.fore_color.rgb = rgb(BG)
    for nm in ('title', 'page'):
        el = copy.deepcopy(shape_by_name(S[26], nm)._element)
        s27.shapes._spTree.append(el)
    set_title_text(s27, 'Backup: recursive DFS recap (demo fallback)')
    pg = shape_by_name(s27, 'page').text_frame.paragraphs[0].runs
    pg[0].text = '27'
    points(s27, [('Same graph, another question', 'recursive DFS from S on the Dijkstra example'),
                 ('The final frame replays the DFS tree', 'glow and streak in visit order: S → A → T, then S → B'),
                 ('Different from Dijkstra’s hover', 'a recap of the traversal, not a path query')])
    media_slide(s27, mp4=mp4, poster=poster, cap=NEW_CAP)
    S[27] = s27
    LOG.append('27 added: DFS recap backup')

# ======================= speaker notes for the media slides =======================
MEDIA = f'{GH}presentation/ca-2026-11-16-deck-media/'
import json as _json
_man = _json.loads((NEW / 'manifest.json').read_text(encoding='utf-8'))


def narration(slug):
    for a in _man.get('assets', []):
        if a.get('file', '').endswith(slug + '.mp4'):
            return list(a.get('narration_en') or a.get('narration') or [])
    return []


V10B_LINES = narration('02b_v10_split_left_bottom')
LCA_POSTER_TEXT = 'the frame with the "differ · lift both" note.'
LCA_SECONDS = next((round(a.get('durationSeconds'), 1) for a in _man.get('assets', []) if a.get('file', '').endswith(LCA_CLIP + '.mp4')), '')
PAR_POSTER = 'the graph with both B → A edges, labelled 5 and 2.'
PAR_EXTRA = ('\nLive force layout was off, so only the dragged vertex moved. An edge drawn on the canvas starts without a weight '
             '(the app counts it as 1 and says so) until one is typed in the Edges text, which applies as you type.')
V10B_POSTER = 'Status docked under the drawing at frame 12 of 21.'


def clip_block(lines, poster_text, extra=''):
    return 'CLIP (press → or click the video; it plays once)\n' + '\n'.join(lines) + f'\nPoster if the video cannot play: {poster_text}' + extra


if V10_CLIP.startswith('02b'):
    v10_action = ('[Press → to play the clip: the Status tab splits the right group in two, joins the left group, '
                  'then docks under the drawing, while the run stays at frame 12.]')
    v10_block = clip_block(V10B_LINES, V10B_POSTER,
                           '\nSet up before recording, also by a real drag: Status was put beside Pseudocode as a tab. '
                           'The default layout has them as two groups.')
    v10_alt = (f'\n\nEARLIER CLIP (not on the slide)\n{MEDIA}clips/02_v10_move_panel.mp4 (7.3 s) moves Status to the left group '
               'and then uses Settings > Reset panel layout.')
else:
    v10_action = ('[Press → to play the clip: Status moves into the left group while the run stays at frame 12, '
                  'then Reset panel layout puts it back.]')
    v10_block = clip_block(['0.0-1.0 s: Dijkstra paused at frame 12 of 21; Status is in the lower right.',
                            '1.0-2.6 s: the Status tab is dragged onto the left group; the drop preview outlines that group.',
                            '2.6-4.5 s: Status is now a tab beside Action and E-Lecture; still frame 12, and the drawing has not moved.',
                            '4.5-5.7 s: Settings, then Reset panel layout, puts Status back in the lower right.',
                            '5.7-7.3 s: the run is still at frame 12.'], 'Status in the left group at frame 12.')
    v10_alt = ''
set_notes(S[14], f"""Bao | Algorithm Visualizers | 70 seconds including the clip

The V10 shell is a stateful layout system. Moving a panel must preserve the canvas and the panel's input state. The layout model keeps groups in the left, right and bottom regions and enforces size constraints. One resolver handles the geometry used for both the displayed layout and drop previews. This helps the preview match what the user will get after releasing the tab. Saved layouts are versioned and checked when loaded, with repair or a default when needed. Each visualizer supplies its own panels and minimum drawing space. {v10_action} The implementation trades the freedom of a completely general split layout for a stable drawing area and predictable interactions.

{v10_block}{v10_alt}

LIVE ALTERNATIVE
Only if time allows: move one tab while paused, show the unchanged canvas and frame, then Settings > Reset panel layout.

SOURCE
{GH}03_architecture_and_decisions.md
Media: {MEDIA}clips/{V10_CLIP}.mp4 (app 346e84b, recorded 16 Nov 2026; manifest.json in that folder)""")

if PAR:
    set_notes(S[15], f"""Bao | Algorithm Visualizers | 65 seconds including the clip

Moving a vertex changes the drawing. Changing an edge weight changes the problem the algorithm is solving. So I keep the graph document, layout, playback session and presentation separate, as listed on the slide. [Press → to play the clip.] Dragging B preserves the current step: the counter stays at 12. Changing the weight of B to A from 1 to 5 edits the document, so the old run is invalidated and the footer says No run. Then I draw a second edge from B to A on the canvas; it appears in the text too, where I give it weight 2. The two parallel edges are separate edges, each with its own identity and weight, for the editor, the drawing and the algorithms. The aim is consistent interaction backed by clear state ownership.

{clip_block(narration('03b_graph_drag_edit_parallel'), PAR_POSTER, PAR_EXTRA)}

EARLIER CLIP (not on the slide)
{MEDIA}clips/03_graph_drag_then_edit.mp4 (8.0 s) stops after the weight edit.

SOURCE
{GH}docs/CA_PRESENTATION_GRAPH_CASE.md
Media: {MEDIA}clips/03b_graph_drag_edit_parallel.mp4 (app 346e84b, recorded 16 Nov 2026). Codex's earlier clip presentation/ca-2026-11-16/02_short_clips/01_graph_paused_step.mp4 shows a similar paused drag.""")
else:
  set_notes(S[15], f"""Bao | Algorithm Visualizers | 65 seconds including the clip

Moving a vertex changes the drawing. Changing an edge weight changes the problem the algorithm is solving. I separate the graph document, layout, playback session and presentation. The document contains nodes, edges and weights. Layout contains positions. A session records the run and selected step. Presentation derives the visible highlights and badges from that step. [Press → to play the clip.] Dragging B preserves the current step: the counter stays at 12. Changing the weight of B to A from 1 to 5 edits the document, so the old run is invalidated and the footer says No run. We cannot keep showing a result for the wrong input. Stable edge identity also lets us distinguish parallel edges. The aim is consistent interaction backed by clear state ownership.

{clip_block(['0.0-0.8 s: Dijkstra paused at frame 12 of 21, relaxing B -> A (weight 1).',
             '0.8-1.8 s: vertex B is dragged a short way; the frame stays 12 of 21.',
             '1.8-3.0 s: hold: same frame, same Status.',
             '3.0-4.5 s: Draw graph opens; the 1 of "B A 1" is selected in the Edges text.',
             '4.5-8.0 s: typing 5 commits the edit: the edge label reads 5, the footer says NO RUN and Status says NO ACTIVE RUN.'],
            'the graph after the edit (B -> A is 5, NO RUN).', '\nLive force layout was off, so only the dragged vertex moved. The app has no on-canvas weight edit; the Edges text applies as you type.')}

SOURCE
{GH}docs/CA_PRESENTATION_GRAPH_CASE.md
Media: {MEDIA}clips/03_graph_drag_then_edit.mp4 (app 346e84b, recorded 16 Nov 2026). Codex's earlier clip presentation/ca-2026-11-16/02_short_clips/01_graph_paused_step.mp4 shows a similar paused drag.""")

set_notes(S[16], f"""Bao | Algorithm Visualizers | 115 seconds including the clip

Binary Lifting is one of the topics I added. A query has several stages and reads an ancestor table. [Press → to play the clip.] I start from a ten-node tree rooted at 10 and move the root to 16 with one control; the same edges are laid out again under the new root. Then I ask for the LCA of 8 and 20. First the deeper node must catch up: the gap is 2, so at k = 1, 8 lifts two levels to 4. Then the two cursors look for the highest ancestors that differ. At k = 3, 2 and 1 both candidates are 16, so they stay. At k = 0 the candidates are 10 and 18, so both lift, and their shared parent, 16, is the answer. In this run no node ever moves, and five of the twelve steps only decide to stay. Without a note, those steps look the same. With floating text, the reason sits beside the node, so the learner can read it without leaving the tree. Status keeps the full sentence, and the pseudocode and the table reads agree with it. During the Week 10 trial, I observed that less experienced users depended heavily on Status, especially for algorithms with several stages such as LCA. Floating text is my design response. We still need to evaluate whether it reduces attention switching. The same rooted tree and ancestor queries are also groundwork for more advanced tree topics later.

{clip_block(narration(LCA_CLIP), LCA_POSTER_TEXT,
            chr(10) + 'Set up before recording, through the real controls: preset Balanced · 10 nodes, u = 8, v = 20. The re-root from 10 to 16, under Edit tree → Structure → Root, is in the clip. '
            'The left column of the slide shows three of the notes, cropped from stills of frames 4, 8 and 9 of the same run. '
            f'The clip is {LCA_SECONDS} s long; keep talking over it.')}

EARLIER CLIPS (not on the slide)
{MEDIA}clips/01c_lca_reroot_8_20.mp4 is the same query without the re-root on camera. {MEDIA}clips/01b_lca_keep_then_jump.mp4 shows LCA(6, 10) = 8 on the default tree (keep at k = 1, lift at k = 0). {MEDIA}clips/01_lca_equal_ancestors.mp4 shows LCA(6, 2) = 4, where every step keeps u and v, then a hover on 6 shows its 2^k ancestors.

SOURCE
{GH}report/week10_user_trial_addendum.md
Media: {MEDIA}clips/{LCA_CLIP}.mp4 (app 346e84b, recorded 16 Nov 2026); stills in {MEDIA}stills/
Historical still of LCA(6, 2): {GH}figures/F5-lca-query-6-2-frame2-note.png (app 662e7b3)""")

set_notes(S[17], f"""Bao | Algorithm Visualizers | 60 seconds including the clip

Sorting comparison gives every pane the same input while keeping its execution state independent. A shared clock advances the active panes by logical operations. They can show different actions and finish at different times. Generators produce operations as needed. Upcoming operations use bounded buffering, while retained history supports backward seeking. Keeping that history has a memory cost on long runs. [Press → to play the clip.] The counters describe the visualization's operations. They are not CPU runtime measurements, and equal operation indices do not guarantee equal computational cost. This makes the comparison useful for examining behavior, while keeping the interpretation honest.

CLIP (Codex pack; press → or click the video; about 10 s)
Bubble Sort and Selection Sort receive the same 12 values (8, 3, 10, 1, 6, 4, 12, 2, 9, 5, 11, 7) at 12 operations per second. Both panes pause together at operation 48 (Bubble: 27 compares, 19 swaps; Selection: 40 compares, 4 swaps), resume together, and Last seeks to the end (Bubble finishes after 92 operations, Selection after 86). The clip length is not a timing result.
Poster if the video cannot play: both panes at operation 48.

LIVE ALTERNATIVE
Only if time allows: step backward once with Prev to show retained history.

SOURCE
{GH}docs/CA_PRESENTATION_CONTRIBUTION_MAP.md
Media: {GH}presentation/ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4 (Codex pack, app 346e84b)""")

if DIJ_CLIP.startswith('04b'):
    set_notes(S[18], f"""Bao | Algorithm Visualizers | 80 seconds including the clip

I also separate visual emphasis from algorithm progress. This is Dijkstra from vertex 0 on visualgo.net's nine-vertex "Big" example. [Press → to play the clip.] The run is paused at frame 17, where the algorithm inspects edge 2 to 3. The edge streak and the glow keep moving, but the frame counter stays at 17. They emphasize the current relationship without advancing the computation, which helps the learner inspect it for longer. Kerk suggested this paused motion; I implemented it. When I press Next, the step arrives with a short note beside 3: 12 plus 14 is less than 33, so update. The badge on 3 changes from 33 to 26, and Status says the same. Floating text handles the arrival of a step; paused motion handles waiting on it. These are different mechanisms. At the final frame, hovering 8 shows its computed shortest path, 0 to 2 to 3 to 8, distance 42; hovering 4 shows 0 to 2 to 3 to 4, distance 46. Both go through 3 by way of 2, not along the direct-looking arc from 1 to 3. The application derives the highlight from the stored result; it does not rerun. DFS has a different final behavior, a moving recap of the visit order and traversal tree, which we show in the demo. Motion can be turned off, and reduced-motion behavior matters for accessibility.

{clip_block(narration('04b_dijkstra_big_note_pause_hover'), 'frame 18 of 53 with the 2 → 3 update note.',
            '\nThe paused motion is subtle over Zoom: point at the 2 → 3 edge while the counter reads 17. Edge weights are small at slide size; read them out if asked. Headless capture shows no mouse pointer; the hovers are real.')}

EARLIER CLIP (not on the slide)
{MEDIA}clips/04_dijkstra_note_pause_hover.mp4 shows the same sequence on the four-vertex S, A, B, T graph used on slide 15.

SOURCE
{GH}docs/CA_PRESENTATION_INTERACTIVE_DEMO.md
Media: {MEDIA}clips/04b_dijkstra_big_note_pause_hover.mp4 (app 346e84b, recorded 16 Nov 2026; preset Big, visualgo.net's TESSELLATION example)""")
else:
  set_notes(S[18], f"""Bao | Algorithm Visualizers | 80 seconds including the clip

I also separate visual emphasis from algorithm progress. [Press → to play the clip.] While the run is paused, the frame counter stays at 11, but the edge streak and the glow on B keep moving. They emphasize the current relationship without advancing the computation, which helps the learner inspect it for longer. When I press Next, the step arrives with a short note above A, "1 + 1 < 4, update", and it agrees with Status. Floating text handles the arrival of a step; paused motion handles waiting on it. These are different mechanisms. At Dijkstra's final frame, hovering T shows its computed shortest path, S to B to A to T, distance 4; hovering A shows distance 2. The application derives that highlight from the stored result; it does not rerun. DFS has a different final behavior, a moving recap of the visit order and traversal tree, which we show in the demo. Motion can be turned off, and reduced-motion behavior matters for accessibility.

{clip_block(['0.0-2.5 s: paused at frame 11 of 21 (inspect edge B -> A, weight 1); the edge streak and B’s glow keep moving while the counter stays at 11.',
             '2.5-4.7 s: Next, frame 12: "1 + 1 < 4 · update" appears above A; Status says A’s distance becomes 2.',
             '4.7-5.9 s: Last, frame 21 of 21: complete, 4 nodes settled.',
             '5.9-7.9 s: hover T: S -> B -> A -> T, distance 4.',
             '7.9-10.2 s: hover A: S -> B -> A, distance 2.'], 'frame 12 with the note.',
            '\nThe paused motion is subtle over Zoom: point at the B -> A edge while the counter shows 11. Headless capture shows no mouse pointer; the hovers are real.')}

SOURCE
{GH}docs/CA_PRESENTATION_INTERACTIVE_DEMO.md
Media: {MEDIA}clips/04_dijkstra_note_pause_hover.mp4 (app 346e84b, recorded 16 Nov 2026)""")

set_notes(S[24], notes_get(S[24]).replace('{CLIP24}', clip_block(
    ['0.0-1.5 s: the Insert 5 preview is complete at frame 8 of 8; node 5 is marked INSERTED and Apply insertion is shown, but the tree text still has its 6 original lines.',
     '1.5-3.3 s: Previous twice: frame 7 creates node 5 under 6; frame 6 compares 5 with 6.',
     '3.3-5.2 s: Next twice returns to frame 8 of 8, where Apply insertion shows again.',
     '5.2-6.2 s: Apply insertion ends the run (NO RUN); node 5 stays as an ordinary node.',
     '6.2-8.6 s: Edit tree opens; the text now ends with "6 5" (8 nodes, 7 edges).'],
    'the completed preview with the Apply insertion button.',
    f'\nMedia: {MEDIA}clips/05_bst_preview_apply.mp4 (app 346e84b, recorded 16 Nov 2026)')))

notes_replace(S[20], 'Avoid repeating the full floating-text explanation.',
              'Avoid repeating the full floating-text explanation. Fallback: if a live step fails, use the clips on slides 15-18, '
              'or the recursive DFS recap, the first slide of the backup file; do not debug during the talk.')
notes_replace(S[20], 'DEMO CUE\n', 'DEMO CUE (a working plan to settle in rehearsal; the slide itself only says "Live demo")\n')

if 27 in S:
    set_notes(S[27], f"""Both | Backup | demo fallback

Use this slide only if the live Graph Editor part of the demo on slide 20 fails. Recursive DFS runs on the same S, A, B, T graph as the Dijkstra part of the demo. On its final frame, the drawing replays the DFS tree in visit order every few seconds: S to A to T, then S to B. This is a different final behaviour from Dijkstra's hover path.

{clip_block(['0.0-0.8 s: recursive DFS from S at frame 1 of 21.',
             '0.8-8.5 s: Last, frame 21 of 21: complete, visited S, A, T, B; a glow and a light streak replay the DFS tree in visit order about every 3 s.'],
            'the final frame of the DFS run.')}

SOURCE
{GH}docs/CA_PRESENTATION_INTERACTIVE_DEMO.md
Media: {MEDIA}clips/06_dfs_recursive_recap.mp4 (app 346e84b, recorded 16 Nov 2026)""")

set_notes(S[26], notes_get(S[26]).replace('slides 1, 2, 8, 14-19 and 24 use real captures',
                                          'slides 1, 2, 8, 13-19, 24 and 27 use real captures'))

import re as _re
for n in (14, 15, 16, 17, 18, 20, 24, 26, 27):
    if n in S:
        t = notes_get(S[n]).replace(' -> ', ' → ').replace('B -> A', 'B → A')
        t = _re.sub(r'(\d+\.\d)-(\d+\.\d) s', r'\1–\2 s', t)
        t = t.replace('slides 15-18', 'slides 15–18').replace('slides 7-12', 'slides 7–12').replace('15-16 November', '15–16 November')
        t = t.replace('13-19', '13–19')
        set_notes(S[n], t)

early26 = ('Slide 5 uses the standalone prototype builds, rebuilt at their last documented commits and captured on '
           '16 November 2026 (presentation/ca-2026-11-16-deck-media/early-prototypes/). ') if EARLY_READY else ''
set_notes(S[26], notes_get(S[26]).replace('{EARLY26}', early26))

# ======================= order: Sorting before LCA =======================
# Bao's choice of 16 November: Sorting stands apart, so it comes before the two
# explanation slides (LCA, then Dijkstra). In this script S[16] is still the LCA
# slide and S[17] the Sorting slide, as in the draft; only the final order changes.
SWAP_16_17 = True
if SWAP_16_17:
    ids = prs.slides._sldIdLst
    els = list(ids)
    sort_el = els[16]
    ids.remove(sort_el)
    ids.insert(15, sort_el)
    for sl, num in ((S[17], '16'), (S[16], '17')):
        shape_by_name(sl, 'page').text_frame.paragraphs[0].runs[0].text = num
    LOG.append('order: Sorting is slide 16, LCA is slide 17')

# ======================= two files: the main deck and the Q&A backup =======================
# Bao's choice of 16 November: the main deck ends on Questions (slide 23). The four
# backup slides go to a second file, with the DFS recap first because it is the
# fallback for the live demo.
BACKUP_OUT = Path(sys.argv[3]) if len(sys.argv) > 3 else None
if BACKUP_OUT is None:
    prs.save(str(OUT))
else:
    n26 = notes_get(S[26])
    for old26, new26 in (
            ('slides 1, 2, 8, 13–19, 24 and 27 use real captures of app 346e84b',
             'in the main deck, slides 1, 2, 8 and 13–19 use real captures of app 346e84b, and so do the first two slides of this backup file,'),
            ('Slide 25 uses a historical capture', 'The correctness slide of this file uses a historical capture'),
            ('Media in this deck:', 'Media:')):
        if old26 not in n26:
            raise SystemExit(f'slide 26 notes: text not found: {old26[:50]!r}')
        n26 = n26.replace(old26, new26)
    set_notes(S[26], n26)
    # the Questions slide says where the backup slides are
    notes_replace(S[23], '\n\nSOURCE',
                  '\n\nBACKUP FILE (open it before the talk)\n'
                  'VisuAlgo_CA_QA_Backup.pptx holds four slides for Q&A: B1 recursive DFS recap (also the fallback for the live demo), '
                  'B2 preview before Apply (BST), B3 correctness and limitations, B4 evidence and ownership.'
                  '\n\nSOURCE')
    full = OUT.with_name(OUT.stem + '.full.pptx')
    prs.save(str(full))

    def keep_slides(path_out, keep, pages=None):
        q = Presentation(str(full))
        ids = q.slides._sldIdLst
        els = list(ids)
        for i, el in enumerate(els):
            ids.remove(el)
            if i not in keep:
                q.part.drop_rel(el.rId)
        for i in keep:
            ids.append(els[i])
        if pages:
            for sl, label in zip(q.slides, pages):
                shape_by_name(sl, 'page').text_frame.paragraphs[0].runs[0].text = label
        q.save(str(path_out))

    keep_slides(OUT, list(range(23)))
    # after the swap above the backups sit at 23 (BST), 24 (correctness), 25 (evidence), 26 (DFS recap)
    keep_slides(BACKUP_OUT, [26, 23, 24, 25], pages=['B1', 'B2', 'B3', 'B4'])
    full.unlink()
    LOG.append(f'main deck: 23 slides; backup file: 4 slides ({BACKUP_OUT.name})')

print('\n'.join(LOG))
print('saved', OUT)
