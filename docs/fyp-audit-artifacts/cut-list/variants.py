import sys,os,shutil
B=chr(92); NL=chr(10)
src_dir,out_root=sys.argv[1],sys.argv[2]
base=open(os.path.join(src_dir,'main.tex'),encoding='utf-8').read()
def rep(t,old,new,count=1):
    if old not in t: raise SystemExit('NOT FOUND: '+old[:70])
    return t.replace(old,new,count)
def cut_between(t,start,end_incl):
    i=t.index(start); j=t.index(end_incl,i)+len(end_incl)
    return t[:i]+t[j:]
def e1(t):  # drop back matter (page 16)
    i=t.index(B+'vfill'+NL+B+'noindent'+B+'footnotesize'+B+'textbf{Report scope')
    j=t.index(B+'end{document}')
    return t[:i]+t[j:]
def e2(t):  # flexible floats, no forced page breaks
    t=t.replace('{figure}[H]','{figure}[tbp]').replace('{table}[H]','{table}[tbp]')
    t=rep(t,B+'newcommand{'+B+'page}{'+B+'par'+B+'penalty0 '+B+'ifdim'+B+'pagetotal>.72'+B+'textheight'+B+'clearpage'+B+'else'+B+'vspace{8pt}'+B+'fi}',B+'newcommand{'+B+'page}{'+B+'par'+B+'vspace{8pt}}')
    return t
def e3(t):  # prose de-duplication
    cuts=[
     ' It does not establish the current quality of VisuAlgo+ or prove that a shared shell is educationally superior. Those claims require evaluation of this implementation.',
     ' The Week 10 trial provided initial usability feedback; systematic follow-up remains necessary.',
     ' These responsibilities overlap at integration boundaries and are not inferred from commit counts alone.',
     ' This is not an unconditional guarantee on very small windows.',
     ' The current automated coverage of those interactions is incomplete.',
     ' Persistent Status text remains available, so the short-lived note is supplementary.',
     ' The nearby explanation complements the persistent Status panel.',
     'The design is an implemented response to an explanation problem, not evidence that attention or learning has improved. ',
     ' This is a build observation, not a loading-time benchmark.',
     ' The counts also reflect test organization and should not be treated as a score for development quality. In particular, browser automation does not yet cover the full panel drag-and-split interaction.',
     ' Separate developer checks also lack a complete recorded protocol; they should not be conflated with the Week 10 user trial.',
     ' Presenting the current application as WASM-powered would therefore be inaccurate.',
     ' A small study can identify interaction problems; it cannot establish general learning effectiveness.',
     ' Dates are working windows, not confirmed assessment deadlines.',
    ]
    for c in cuts: t=rep(t,c,'')
    t=rep(t,' The audit also recorded 266 CI runs, including eight failed runs followed by successful runs of the relevant workflows~'+B+'cite{validation}.','')
    t=rep(t,' These labels describe catalogue coverage, not complete operation parity or educational validation~'+B+'cite{validation}.','~'+B+'cite{validation}.')
    t=cut_between(t,'The survey therefore served as formative input','in the evidence pack.'+NL+NL)
    t=cut_between(t,'After adopting V10, we conducted a separate user trial','earlier V2/V7 survey.')
    t=rep(t,'On 18 October, Kerk consolidated','A formative user trial of V10 in Week 10 (Section 6.1) informed later refinements, including floating text. On 18 October, Kerk consolidated')
    t=cut_between(t,'The graph and tree canvases use React Flow, with D3 handling','useful existing visualization libraries.'+NL+NL)
    t=cut_between(t,'The architecture provides a place for later engine integration','remain concrete integration tasks.'+NL+NL)
    t=cut_between(t,'The flexibility also creates additional failure cases','priority for the next phase.')
    t=rep(t,'This account follows my clarification on 4 November 2026. A shared-folder screenshot shows prototype-testing video files, but participant numbers, test questions, scores, detailed feedback and coded observations are not included here.','The session videos, test responses and feedback have not yet been analysed, so participant numbers, scores and detailed findings are not reported here.')
    t=cut_between(t,'1--3 November & Recorded validation','updated.'+B+B)
    return t
def e4(t):  # drop Figure 9 (catalogue viewport screenshot)
    return cut_between(t,B+'shot{F1-home-catalogue.png}','{fig:home}')
variants={'v1_backmatter':[e1],'v2_backmatter_floats':[e1,e2],'v3_plus_prose':[e1,e2,e3],'v4_plus_dropF9':[e1,e2,e3,e4],'v5_prose_only_keepH':[e1,e3]}
for name,fs in variants.items():
    t=base
    for f in fs: t=f(t)
    d=os.path.join(out_root,name); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'main.tex'),'w',encoding='utf-8').write(t)
    shutil.copy(os.path.join(src_dir,'references.bib'),d)
    if not os.path.exists(os.path.join(d,'figures')): shutil.copytree(os.path.join(src_dir,'figures'),os.path.join(d,'figures'))
    print('wrote',name,len(t))
