"""Write the speaking script into the master script and the cheat sheet.

Run from the docsforfyp repository root:
    py -3.12 presentation/ca-2026-11-16-deck-media/deck-build/make_script_docs.py

speaking_script.json is the source. For every slide the master script gets a main
message, talking points, the script, cues and a transition, followed by a folded
block with the slide text, clip details and sources that were already there. The
cheat sheet gets the message, the talking points and the transition, plus the cues
on the clip and demo slides. Running it again replaces what it wrote before.
"""
import io
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MASTER = Path('presentation/VisuAlgo_CA_Master_Script.md')
CHEAT = Path('presentation/VisuAlgo_CA_Cheat_Sheet.md')
WPM = 130
SPEAK = json.loads((HERE / 'speaking_script.json').read_text(encoding='utf-8'))['slides']
CUES_ON_SHEET = {'14', '15', '16', '17', '18', '20', 'B1', 'B2'}
SUMMARY = 'Slide text, clip details and sources'


def words(entry):
    text = ' '.join(re.sub(r'\[[^\]]*\]', '', p) for p in entry['script'] + [entry.get('transition', '')])
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’+.,-]*", text))


def script_md(entry):
    out = []
    for para in entry['script']:
        m = re.match(r'(Bao|Kerk): (.*)', para, flags=re.S)
        out.append(f'> **{m.group(1)}:** {m.group(2)}' if m else f'> {para}')
    return '\n>\n'.join(out)


def speak_block(entry, slot_seconds):
    n = words(entry)
    fit = f'*Script: {n} words, about {round(n / WPM * 60)} s at {WPM} words per minute'
    fit += f'; the slot is {slot_seconds} s.*' if slot_seconds else '.*'
    out = [fit,
           f"**Main message:** {entry['message']}",
           '**Talking points**\n\n' + '\n'.join('- ' + p for p in entry['points']),
           '**Script**\n\n' + script_md(entry)]
    if entry.get('cues'):
        out.append('**Cues**\n\n' + '\n'.join('- ' + c for c in entry['cues']))
    if entry.get('transition'):
        out.append(f"**Transition:** {entry['transition']}")
    return '\n\n'.join(out)


def seconds(header):
    m = re.search(r'(\d+):(\d+)[–-](\d+):(\d+)', header)
    return (int(m.group(3)) * 60 + int(m.group(4))) - (int(m.group(1)) * 60 + int(m.group(2))) if m else None


raw = io.open(MASTER, encoding='utf-8', newline='').read()
crlf = '\r\n' in raw
text = raw.replace('\r\n', '\n')
parts = re.split(r'\n(?=###? )', text)
headers = {}
done = 0
for i, part in enumerate(parts):
    m = re.match(r'### (\w+)\. (.*)\n', part)
    if not m:
        continue
    key = m.group(1).lstrip('0') or '0'
    if key not in SPEAK:
        raise SystemExit(f'no speaking script for section {m.group(1)}')
    entry = SPEAK[key]
    lines = part.rstrip('\n').split('\n')
    hi = next(j for j, ln in enumerate(lines) if j > 0 and ln.startswith('**'))
    header = lines[hi]
    headers[key] = (m.group(2).strip(), header.strip('*'))
    body = '\n'.join(lines[hi + 1:]).strip('\n')
    if '<details>' in body:  # written by an earlier run: keep only the folded reference
        ref = body[body.index('<details>'):]
        ref = re.sub(r'^<details>\n<summary>[^\n]*</summary>\n\n', '', ref)
        ref = re.sub(r'\n\n</details>\s*$', '', ref)
    else:
        a = body.index('**English script**')
        ends = [body.find(tag, a) for tag in ('**Delivery cue:**', '**Team review:**', '**Source:**', '**Media:**', '**Backup file:**')]
        b = min(e for e in ends if e != -1)
        ref = (body[:a] + body[b:]).strip('\n')
    for label in entry.get('drop_blocks', []):  # an old cue that the new cues replace
        if label == 'DEMO CUE':
            ref = re.sub(r'\*\*Delivery cue:\*\*[^\n]*\n\n', '', ref)
    new = '\n\n'.join([lines[0], header, speak_block(entry, seconds(header)),
                       f'<details>\n<summary>{SUMMARY}</summary>\n\n{ref}\n\n</details>'])
    parts[i] = new + '\n'
    done += 1
text = '\n'.join(parts)

FORMAT = ('Script format, 16 November, at Bao\'s request: every slide has a main message, three to five talking points, '
          'a script in plain spoken English, cues and a transition to the next slide. The talking points are there so the '
          'speaker can say it in their own words; the script is not meant to be learned by heart. The slide text, clip '
          'timings and sources are folded under each script. The same text is in the speaker notes of both PowerPoint '
          'files, and [the cheat sheet](VisuAlgo_CA_Cheat_Sheet.md) has the short version. The word counts assume about '
          f'{WPM} words per minute and are a guide, not a measurement. Kerk\'s slides, 7 to 12, were reworded in the same '
          'style with their technical content kept; they are his to confirm.')
if 'Script format, 16 November' in text:
    text = re.sub(r'Script format, 16 November[^\n]*', lambda m: FORMAT, text)
else:
    anchor = '\n\nOwner confirmations:'
    if text.count(anchor) != 1:
        raise SystemExit('master script: intro anchor not found')
    text = text.replace(anchor, '\n\n' + FORMAT + anchor)
io.open(MASTER, 'w', encoding='utf-8', newline='').write(text.replace('\n', '\r\n') if crlf else text)
print(f'{MASTER}: {done} sections written')

# ---------------------------------------------------------------- cheat sheet
sheet = ['# VisuAlgo+ CA talk: cheat sheet', '',
         'One glance per slide: the message, the points to hit and the line that leads to the next slide. '
         'Clip and demo slides also list their cues. The full wording is in [the master script](VisuAlgo_CA_Master_Script.md) '
         'and in the speaker notes. Both come from `ca-2026-11-16-deck-media/deck-build/speaking_script.json`.', '',
         '33 minutes of talk, then 12 minutes of questions. Slides 7 to 12 are Kerk\'s; 20 to 23 are shared.', '']
for key, entry in SPEAK.items():
    title, header = headers[key]
    num = key if key.startswith('B') else f'{int(key):02d}'
    who = re.sub(r'^Backup / [^,]*, outside timed talk$', 'Backup', header)
    sheet += [f'## {num} · {title}', '', f'*{who}*', '', f"**Message:** {entry['message']}", '']
    sheet += ['- ' + p for p in entry['points']]
    if key in CUES_ON_SHEET and entry.get('cues'):
        sheet += ['', '**Cues**', ''] + ['- ' + c for c in entry['cues']]
    if entry.get('transition'):
        sheet += ['', f"**Next:** {entry['transition']}"]
    sheet.append('')
io.open(CHEAT, 'w', encoding='utf-8', newline='\n').write('\n'.join(sheet))
print(f'{CHEAT}: {len(SPEAK)} slides')
