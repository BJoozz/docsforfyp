// Writes presentation/VisuAlgo_CA_Reading_Script.docx: the slide titles and the spoken script only,
// for reading practice. speaking_script.json (next to this file) is the source.
//
// Run from the docsforfyp repository root. It needs the `docx` npm package; if it is not installed
// next to this file, install it anywhere and point NODE_PATH at that node_modules folder:
//     node presentation/ca-2026-11-16-deck-media/deck-build/make_reading_script.js
const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Footer, PageNumber, AlignmentType } = require('docx');

const SPEAK = JSON.parse(fs.readFileSync(path.join(__dirname, 'speaking_script.json'), 'utf8')).slides;
const OUT = process.argv[2] || 'presentation/VisuAlgo_CA_Reading_Script.docx';
const NAVY = '142B43', TEAL = '087F8C', MUTED = '637587';

// spoken words in black; [stage directions] and speaker tags set apart
function runs(text, italics = false) {
  const out = [];
  const m = text.match(/^(Bao|Kerk): /);
  if (m) {
    out.push(new TextRun({ text: m[1] + ': ', bold: true, color: TEAL }));
    text = text.slice(m[0].length);
  }
  for (const part of text.split(/(\[[^\]]*\])/)) {
    if (!part) continue;
    out.push(/^\[.*\]$/.test(part)
      ? new TextRun({ text: part, italics: true, color: MUTED, size: 22 })
      : new TextRun({ text: part, italics }));
  }
  return out;
}

function slide(key, e) {
  const num = key.startsWith('B') ? key : String(key).padStart(2, '0');
  const when = e.time === 'backup' ? 'backup slide' : e.time;
  const out = [
    new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: `${num} · ${e.title}` })] }),
    new Paragraph({ keepNext: true, spacing: { after: 140, line: 276 }, children: [new TextRun({ text: `${e.speaker} · ${when}`, color: MUTED, size: 20 })] }),
  ];
  // the line that leads to the next slide stays with the paragraph before it
  e.script.forEach((para, i) => out.push(new Paragraph({ keepNext: Boolean(e.transition) && i === e.script.length - 1, children: runs(para) })));
  if (e.transition) out.push(new Paragraph({ children: runs(e.transition, true) }));
  return out;
}

const keys = Object.keys(SPEAK);
const main = keys.filter((k) => !k.startsWith('B'));
const groups = [
  ['Bao', main.filter((k) => SPEAK[k].speaker === 'Bao')],
  ['Kerk', main.filter((k) => SPEAK[k].speaker === 'Kerk')],
  ['Questions and backup slides', main.filter((k) => SPEAK[k].speaker === 'Both').concat(keys.filter((k) => k.startsWith('B')))],
];
const body = [
  new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun({ text: 'VisuAlgo+ CA talk: reading script' })] }),
  new Paragraph({ spacing: { after: 80, line: 276 }, children: [new TextRun({ text: 'Slide titles and the spoken script only, in the order of the deck. 16 November 2026, 33 minutes.', color: MUTED, size: 22 })] }),
  new Paragraph({ spacing: { after: 200, line: 276 }, children: [new TextRun({ text: 'Words in [brackets] are actions, not speech. The last line of a slide, in italics, leads to the next slide.', color: MUTED, size: 22 })] }),
];
groups.forEach(([name, ks], i) => {
  const first = ks[0], last = ks[ks.length - 1];
  const label = name === 'Bao' || name === 'Kerk' ? `${name}: slides ${first} to ${last}` : name;
  body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: i > 0, children: [new TextRun({ text: label })] }));
  for (const k of ks) body.push(...slide(k, SPEAK[k]));
});

const doc = new Document({
  creator: 'VisuAlgo+ CA deck build',
  title: 'VisuAlgo+ CA talk: reading script',
  styles: {
    default: {
      document: { run: { font: 'Arial', size: 26 }, paragraph: { spacing: { line: 348, after: 170 } } },
      title: { run: { font: 'Arial', size: 40, bold: true, color: NAVY }, paragraph: { spacing: { before: 0, after: 100 }, keepNext: true } },
      heading1: { run: { font: 'Arial', size: 32, bold: true, color: TEAL }, paragraph: { spacing: { before: 240, after: 80 }, keepNext: true } },
      heading2: { run: { font: 'Arial', size: 28, bold: true, color: NAVY }, paragraph: { spacing: { before: 360, after: 20 }, keepNext: true } },
    },
  },
  sections: [{
    properties: { page: { margin: { top: 1247, bottom: 1247, left: 1361, right: 1361 } } },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
        children: [new TextRun({ children: ['Page ', PageNumber.CURRENT, ' of ', PageNumber.TOTAL_PAGES], size: 18, color: MUTED })] })] }),
    },
    children: body,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log(`${OUT}: ${keys.length} slides, ${buf.length} bytes`);
});
