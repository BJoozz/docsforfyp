"""Write the speaking script into the speaker notes of a finished deck.

    py -3.12 write_notes.py <in.pptx> <out.pptx> main|backup

speaking_script.json is the source. In the main deck the entries "1", "2", ... go to the
slides in order; in the backup file "B1" to "B4" do. Each note becomes: the speaker line,
MAIN MESSAGE, TALKING POINTS, SCRIPT, CUES and TRANSITION, followed by the reference
blocks the note already had (CLIP, VISUAL, SOURCE and so on). An entry with
"keep_blocks": false drops those blocks, because the slide was remade and they describe
the old one. Nothing on the slides changes, except the few words listed under
"slide_text_fixes" (slide numbers quoted on a backup slide).
"""
import json
import re
import sys
from pathlib import Path

from pptx import Presentation

src, out, which = sys.argv[1], sys.argv[2], sys.argv[3]
DATA = json.loads((Path(__file__).resolve().parent / 'speaking_script.json').read_text(encoding='utf-8'))
SPEAK = DATA['slides']
BLOCK = re.compile(r'^(CLIP|SOURCE|VISUAL|DEMO CUE|EVIDENCE|EARLIER CLIP|CURRENT APP MEDIA|LIVE ALTERNATIVE|BACKUP FILE|TEAM REVIEW)\b')

prs = Presentation(src)
slides = list(prs.slides)
keys = [k for k in SPEAK if k.startswith('B')] if which == 'backup' else [k for k in SPEAK if not k.startswith('B')]
if len(keys) != len(slides):
    raise SystemExit(f'{len(slides)} slides but {len(keys)} script entries')
FIXES = [(a, b) for a, b, where in DATA.get('note_fixes', []) if where == which]
fix_hits = {a: 0 for a, _ in FIXES}


def speaker_line(entry, old_head):
    if entry['seconds']:
        tail = 'including the clip' if any('[Press →' in p for p in entry['script']) else 'including actions'
        return f"{entry['speaker']} | {entry['section']} | {entry['seconds']} seconds {tail}"
    if entry['time'] == 'backup':
        tail = old_head.split('|')[-1].strip() if '|' in old_head else 'outside the timed talk'
        return f"{entry['speaker']} | {entry['section']} | {tail}"
    return f"{entry['speaker']} | {entry['section']} | {entry['time']}"


def split_old(rest):
    """-> (paragraphs that were spoken text or a REFERENCE block, reference blocks to keep)."""
    spoken, kept, mode = [], [], 'speak'
    written_before = bool(rest) and rest[0].strip().startswith('MAIN MESSAGE')
    for para in rest:
        first = para.strip().split('\n')[0]
        if mode != 'kept' and BLOCK.match(first):
            mode = 'kept'
        if mode == 'kept':
            kept.append(para)
        elif not written_before:
            spoken.append(para)
        elif first == 'REFERENCE':
            mode = 'ref'
            body = para.strip()[len('REFERENCE'):].strip('\n')
            if body:
                spoken.append(body)
        elif mode == 'ref':
            spoken.append(para)
    return spoken, kept


def new_notes(entry, old):
    paras = old.split('\n\n')
    old_head = paras[0].split('\n')[0].strip()
    spoken_old, kept = split_old(paras[1:])
    if entry.get('keep_blocks') is False:
        kept = []
    kept = [para for para in kept if not any(para.strip().startswith(d) for d in entry.get('drop_blocks', []))]
    out_paras = [speaker_line(entry, old_head),
                 'MAIN MESSAGE\n' + entry['message'],
                 'TALKING POINTS\n' + '\n'.join('• ' + x for x in entry['points']),
                 'SCRIPT\n' + '\n\n'.join(entry['script'])]
    if entry.get('cues'):
        out_paras.append('CUES\n' + '\n'.join('• ' + x for x in entry['cues']))
    if entry.get('transition'):
        out_paras.append('TRANSITION\n' + entry['transition'])
    if entry.get('keep_old_as'):
        out_paras.append(entry['keep_old_as'] + '\n' + '\n\n'.join(spoken_old))
    text = '\n\n'.join(out_paras + kept)
    for a, b in FIXES:
        if a in text:
            fix_hits[a] += text.count(a)
            text = text.replace(a, b)
        elif b in text:  # already fixed by an earlier run
            fix_hits[a] += 1
    return text


for key, slide in zip(keys, slides):
    entry = SPEAK[key]
    title = next((sh.text_frame.text.strip() for sh in slide.shapes if sh.name == 'title'), '')
    if title != entry['title']:
        raise SystemExit(f'entry {key} is for "{entry["title"]}" but the slide is "{title}"')
    tf = slide.notes_slide.notes_text_frame
    tf.text = new_notes(entry, tf.text)
    for a, b in DATA.get('slide_text_fixes', {}).get(key, []):
        hits = 0
        for sh in slide.shapes:
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    for run in para.runs:
                        if a in run.text:
                            run.text = run.text.replace(a, b)
                            hits += 1
        done_before = any(b in run.text for sh in slide.shapes if sh.has_text_frame
                          for para in sh.text_frame.paragraphs for run in para.runs)
        if hits != 1 and not (hits == 0 and done_before):
            raise SystemExit(f'{key}: expected one run with "{a}", found {hits}')
missed = [a for a, n in fix_hits.items() if n == 0]
if missed:
    raise SystemExit('note_fixes that matched nothing: ' + ' | '.join(m[:60] for m in missed))
prs.save(out)
print(f'notes written for {len(keys)} slides, {sum(fix_hits.values())} slide-number fixes -> {out}')
