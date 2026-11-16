"""Adopt the deck that Kerk rearranged by hand on 16 November 2026.

    py -3.12 adopt_rearranged_deck.py <rearranged.pptx> <out.pptx>

It changes two things and leaves every slide's design alone:
1. The Motivation slide carried five shapes left over from an older version (a card
   number, heading, detail, picture and caption that sat exactly on top of the current
   ones, so the caption read as two overlapping lines). They are removed.
2. The page labels still showed the numbers of the earlier order. They are renumbered
   01, 02, ... in slide order.
The speaker notes are written afterwards by write_notes.py.
"""
import sys

from pptx import Presentation

src, out = sys.argv[1], sys.argv[2]
prs = Presentation(src)
slides = list(prs.slides)


def named(slide, name):
    return [sh for sh in slide.shapes if sh.name == name]


# 1. leftovers on the Motivation slide
mot = [s for s in slides if named(s, 'title') and named(s, 'title')[0].text_frame.text.strip() == 'Motivation']
if len(mot) != 1:
    raise SystemExit('expected exactly one Motivation slide')
mot = mot[0]
removed = []
caps = named(mot, 'capture-source')
if len(caps) == 2:
    old_cap = [c for c in caps if '(app 346e84b)' in c.text_frame.text]
    if len(old_cap) != 1 or old_cap[0] is not caps[1]:
        raise SystemExit('Motivation: the leftover caption is not where it was expected')
    for name in ('number-3', 'point-3', 'detail-3', 'image-3', 'capture-source'):
        pair = named(mot, name)
        if len(pair) != 2:
            raise SystemExit(f'Motivation: expected two shapes named {name}, found {len(pair)}')
        extra = pair[1]  # the leftovers were appended after the current shapes
        extra._element.getparent().remove(extra._element)
        removed.append(name)
elif len(caps) != 1:
    raise SystemExit(f'Motivation: unexpected number of captions: {len(caps)}')
print('Motivation slide: removed leftovers', removed if removed else '(none found)')

# 2. page labels follow the slide order
changed = 0
for n, slide in enumerate(slides, 1):
    page = named(slide, 'page')
    if len(page) != 1:
        raise SystemExit(f'slide {n}: expected one page label, found {len(page)}')
    runs = page[0].text_frame.paragraphs[0].runs
    label = f'{n:02d}'
    if runs[0].text != label or len(runs) > 1:
        runs[0].text = label
        for extra in runs[1:]:
            extra.text = ''
        changed += 1
print(f'page labels: {changed} of {len(slides)} renumbered')
prs.save(out)
print('saved', out)
