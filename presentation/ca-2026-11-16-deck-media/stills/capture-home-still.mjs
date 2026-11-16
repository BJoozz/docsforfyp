// Captures the home page of the app for the deck's title slide.
// Usage: set CA_APP_REPO (the app checkout) and CA_BASE_URL, then
//   node capture-home-still.mjs <output.png>
// It only loads the page: no source edit, no injected state, no CSS and no overlay.
import { createRequire } from 'node:module';
const app = process.env.CA_APP_REPO;
const { chromium } = createRequire(app + '/package.json')('@playwright/test');
const base = process.env.CA_BASE_URL ?? 'http://127.0.0.1:5205';
const out = process.argv[2];
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, locale: 'en-US', reducedMotion: 'no-preference' });
const page = await context.newPage();
const errors = []; page.on('pageerror', (e) => errors.push(e.message));
try {
  await page.goto(base + '/');
  await page.getByText('Editors', { exact: true }).first().waitFor();
  await page.evaluate(async () => { await document.fonts.load('700 14px Inter'); await document.fonts.ready; });
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(800);
  const info = {
    url: page.url(),
    title: await page.title(),
    scrollY: await page.evaluate(() => window.scrollY),
    headings: await page.locator('h1, h2, h3').allInnerTexts(),
    text: (await page.locator('body').innerText()).slice(0, 900),
    imagesLoaded: await page.evaluate(() => [...document.images].every((i) => i.complete && i.naturalWidth > 0)),
    errors,
  };
  await page.screenshot({ path: out });
  console.log(JSON.stringify(info, null, 1));
} finally { await browser.close(); }
