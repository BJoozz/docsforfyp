import { createRequire } from 'node:module';
if (!process.env.CA_APP_REPO) throw new Error('Set CA_APP_REPO to the app checkout.');
const require = createRequire(process.env.CA_APP_REPO + '/package.json');
const { chromium, expect } = require('@playwright/test');
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

// Browser-only evidence capture. Does not edit application source or fake UI state.
const root=process.env.CA_CAPTURE_OUTPUT ?? fileURLToPath(new URL('./recapture/',import.meta.url));
const base=process.env.CA_BASE_URL??'http://127.0.0.1:5205';
const run=process.argv[2]??'graph';
const dirs=['01_main_slides','02_short_clips','03_backup','04_reproduce','raw'];
for(const d of dirs) await mkdir(path.join(root,d),{recursive:true});
const browser=await chromium.launch({headless:true});
const context=await browser.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1,reducedMotion:'no-preference',recordVideo:{dir:path.join(root,'raw'),size:{width:1440,height:900}}});
const recordingStartedAt=Date.now();
const page=await context.newPage();
const errors=[], checks=[];
page.on('pageerror',e=>errors.push(e.message));
async function check(name,data) {checks.push({name,data});console.log(name,JSON.stringify(data));}
async function ready(route){
  await page.goto(base+route);
  if(route!=='/') {await page.locator('.viz-page').waitFor();await page.locator('.workspace-loading__message').waitFor({state:'hidden'});}
  const fonts=await page.evaluate(async()=>{await document.fonts.load('700 14px Inter');await document.fonts.ready;return [...document.fonts].filter(f=>f.family==='Inter'&&f.status==='loaded').length;});
  expect(fonts).toBeGreaterThan(0);
  await page.waitForTimeout(500);
}
const transport=name=>page.locator('.footer-bar').getByRole('button',{name,exact:true});
const frame=()=>page.locator('.footer-bar__frame').innerText();
const status=()=>page.locator('[data-panel-body="status"]').innerText();
async function shot(dir,name,locator){
  const opts={path:path.join(root,dir,name+'.png')};
  if(locator) await locator.screenshot(opts);else await page.screenshot(opts);
  await check('screenshot',{file:dir+'/'+name+'.png',frame:await page.locator('.footer-bar__frame').count()?await frame():null});
}
const node=label=>page.locator('.react-flow__node').filter({has:page.getByText(label,{exact:true})});
async function dragNode(label,to,duration=300){
  const box=await node(label).boundingBox();expect(box).not.toBeNull();
  await page.mouse.move(box.x+box.width/2,box.y+box.height/2);await page.mouse.down();
  const n=12;
  for(let i=1;i<=n;i++){await page.mouse.move(box.x+box.width/2+(to.x-box.x-box.width/2)*i/n,box.y+box.height/2+(to.y-box.y-box.height/2)*i/n);await page.waitForTimeout(duration/n);}
  await page.mouse.up();
}
async function setupGraph(){
  await ready('/graph-editor/dijkstra');
  await page.getByRole('checkbox',{name:'Live force layout',exact:true}).uncheck();
  await page.locator('#graph-nodes-text').fill('S\nA\nB\nT');
  await page.locator('#graph-edges-text').fill('S A 4\nS B 1\nB A 1\nA T 2\nB T 6');
  await page.getByRole('checkbox',{name:'Directed graph',exact:true}).check();
  await page.getByRole('combobox',{name:'Dijkstra start node',exact:true}).selectOption({label:'S'});
  await page.getByRole('combobox',{name:'Dijkstra end node',exact:true}).selectOption({label:'T'});
  await page.getByRole('button',{name:'Draw graph',exact:true}).click();
  if(await page.getByRole('button',{name:'HIDE',exact:true}).isVisible()) await page.getByRole('button',{name:'HIDE',exact:true}).click();
  await page.waitForTimeout(500);
  for(const [label,p] of [['S',{x:445,y:440}],['A',{x:710,y:275}],['B',{x:710,y:595}],['T',{x:980,y:440}]]) await dragNode(label,p);
  await page.mouse.move(320,180);
  await page.waitForTimeout(250);
  await expect(page.locator('.react-flow__node')).toHaveCount(4);
  await expect(page.locator('.react-flow__edge')).toHaveCount(5);
}
try {
  if(run==='graph'){
    await setupGraph();
    const steps=[];
    // Advance via Next, not a scrub: a step note is a forward-arrival effect.
    for(let i=0;i<35;i++){
      await transport('Next').click();
      const s=await status();steps.push({frame:await frame(),status:s});
      if(s.includes('Inspect edge B → A')) break;
    }
    await check('steps_before_note',steps);
    await check('clip_start',{frame:await frame(),status:await status(),time:Date.now()});
    const fixed=await frame();
    const animationBefore=await page.evaluate(()=>document.getAnimations().map(a=>({name:a.animationName,time:a.currentTime})).filter(a=>a.name?.includes('paused')));
    await page.waitForTimeout(2100);
    expect(await frame()).toBe(fixed);
    const animationAfter=await page.evaluate(()=>document.getAnimations().map(a=>({name:a.animationName,time:a.currentTime})).filter(a=>a.name?.includes('paused')));
    await check('paused_frame_and_animation',{frameBefore:fixed,frameAfter:await frame(),animationBefore,animationAfter});
    await transport('Next').click();
    await expect(page.locator('.step-notes')).toContainText('1 + 1 < 4');
    await page.waitForTimeout(280);
    await shot('01_main_slides','02_dijkstra_decision');
    await check('decision',{frame:await frame(),status:await status(),notes:await page.locator('.step-notes').innerText()});
    await page.waitForTimeout(1600);
    const beforeDrag=await frame();
    const b=await node('B').boundingBox();
    await dragNode('B',{x:b.x+b.width/2+35,y:b.y+b.height/2-35},1000);
    await page.mouse.move(320,180);
    expect(await frame()).toBe(beforeDrag);
    await page.waitForTimeout(2200);
    await check('drag_preserves_run',{beforeDrag,afterDrag:await frame()});
    await check('clip_end',{time:Date.now()});
    // End the first recording before preparing still-only final frames.
    await shot('03_backup','graph_paused_after_drag');
    await transport('Last').click();
    await page.waitForTimeout(600);
    await node('T').hover();await page.waitForTimeout(450);
    await shot('01_main_slides','03_dijkstra_final_path_t');
    const final=await frame();
    await check('final_target_t',{frame:final,status:await status()});
    await node('A').hover();await page.waitForTimeout(450);
    await shot('03_backup','01_dijkstra_final_path_a');
    expect(await frame()).toBe(final);
    await check('final_target_a',{frame:await frame(),status:await status()});
    await page.mouse.move(320,180);
    await page.waitForTimeout(200);
    // Real tab drag: inspect target geometry before choosing the bottom region.
    const tab=page.locator('[data-panel-tab="status"]');
    const t=await tab.boundingBox();
    await page.mouse.move(t.x+t.width/2,t.y+t.height/2);await page.mouse.down();
    await page.mouse.move(t.x+t.width/2-25,t.y+t.height/2+25,{steps:5});
    const targets=await page.locator('[data-drop-target]').evaluateAll(es=>es.map(e=>({key:e.dataset.dropTarget,box:e.getBoundingClientRect().toJSON()})));
    await check('layout_drop_targets',targets);
    const bottom=targets.find(t=>t.key.startsWith('bottom')||t.key.includes('bottom'));
    if(!bottom) {await page.keyboard.press('Escape');await page.mouse.up();throw new Error('No bottom drop target');}
    await page.mouse.move(bottom.box.x+bottom.box.width/2,bottom.box.y+bottom.box.height/2,{steps:15});await page.mouse.up();
    await page.waitForTimeout(750);
    const region=await page.locator('[data-panel-body="status"]').evaluate(e=>e.closest('[data-region]')?.dataset.region);
    await check('layout_keeps_run',{before:final,after:await frame(),statusRegion:region});
    expect(region).toBe('bottom');expect(await frame()).toBe(final);
    await shot('01_main_slides','06_v10_layout');
  } else if(run==='tree'){
    await ready('/tree-editor/bst');
    const originalTree=await page.locator('#tree-edges-text').inputValue();
    await page.getByRole('radio',{name:'Insert',exact:true}).click();
    await page.getByRole('textbox',{name:'BST Insert value',exact:true}).fill('5');
    await page.getByRole('button',{name:'Edit tree',exact:true}).click();
    await transport('Next').click();await transport('Last').click();
    await page.waitForTimeout(800);
    await shot('01_main_slides','04_tree_insert_preview');
    const previewText=await page.locator('#tree-edges-text').inputValue();
    expect(previewText).toBe(originalTree);
    await check('tree_preview',{frame:await frame(),status:await status(),nodes:await page.locator('.react-flow__node').count(),committedText:previewText});
    await page.getByRole('button',{name:'Apply insertion',exact:true}).click();
    await page.waitForTimeout(850);
    await shot('03_backup','02_tree_insert_applied');
    const appliedText=await page.locator('#tree-edges-text').inputValue();
    expect(appliedText).not.toBe(originalTree);
    await check('tree_applied',{frame:await frame(),status:await status(),nodes:await page.locator('.react-flow__node').count(),committedText:appliedText});
  } else if(run==='sort'){
    await ready('/sorting');
    await page.getByRole('button',{name:'2',exact:true}).click();
    const dataset=page.getByRole('button',{name:'Dataset',exact:true});
    if(await dataset.getAttribute('aria-expanded')==='false') await dataset.click();
    await page.locator('.sort-setup select').selectOption('custom');
    await page.locator('.sort-setup__field--wide input').fill('8, 3, 10, 1, 6, 4, 12, 2, 9, 5, 11, 7');
    await page.getByRole('button',{name:'Generate',exact:true}).click();
    await page.locator('#sort-pane-algorithm-2').selectOption('selection');
    await page.locator('#sort-pane-algorithm-1').selectOption('bubble');
    await check('sort_ready',{text:await page.locator('.viz-page').innerText()});
    await transport('Next').click();
    // Set a legible continuous demo rate with the app's real slider.
    const speed=page.getByRole('slider',{name:'Target speed',exact:true});
    await speed.fill('4');
    await speed.dispatchEvent('change');
    await check('clip_start',{time:Date.now(),frame:await frame()});
    await transport('Autoplay').click();
    await page.waitForTimeout(4000);
    await transport('Pause').click();
    await page.waitForTimeout(300);
    await shot('01_main_slides','05_sorting_compare');
    await check('sort_mid',{frame:await frame(),panes:await page.locator('.sort-pane').allInnerTexts()});
    await page.waitForTimeout(1100);
    await transport('Autoplay').click();await page.waitForTimeout(3500);
    await transport('Last').click();
    await page.waitForTimeout(900);
    await check('clip_end',{time:Date.now(),frame:await frame()});
  } else if(run==='home'){
    await ready('/');
    const editors=page.getByRole('heading',{name:'Editors',exact:true});
    await editors.scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(root,'01_main_slides','01_editor_entry_points.png'),clip:await page.evaluate(()=>{
      const editor=document.querySelector('.editor-section')??[...document.querySelectorAll('section')].find(e=>e.querySelector('h2')?.textContent==='Editors');
      if(!editor) return {x:0,y:0,width:1440,height:900};
      const r=editor.getBoundingClientRect();return {x:Math.max(0,r.x-15),y:Math.max(0,r.y-15),width:Math.min(1440,r.width+30),height:r.height+30};
    })});
    await check('editor_links',await page.locator('a[href="/graph-editor"],a[href="/tree-editor"]').evaluateAll(es=>es.map(e=>({text:e.innerText,href:e.getAttribute('href')}))));
  }
  expect(errors).toEqual([]);
} catch(error) {
  await page.screenshot({path:path.join(root,'raw',run+'-failed.png')});
  await writeFile(path.join(root,'raw',run+'-failed.txt'),await page.locator('body').innerText());
  throw error;
} finally {
  const video=page.video();
  await context.close();
  const videoPath=await video.path();
  await writeFile(path.join(root,'raw',run+'-checks.json'),JSON.stringify({run,base,recordingStartedAt,closedAt:Date.now(),checks,errors,videoPath},null,2));
  console.log('video',videoPath);
  await browser.close();
}
