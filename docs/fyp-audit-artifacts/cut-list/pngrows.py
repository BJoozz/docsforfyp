import sys,zlib,struct,glob,os
def decode(path):
    d=open(path,'rb').read()
    assert d[:8]==b'\x89PNG\r\n\x1a\n'
    pos=8; idat=b''; w=h=None
    while pos<len(d):
        ln,=struct.unpack('>I',d[pos:pos+4]); typ=d[pos+4:pos+8]; data=d[pos+8:pos+8+ln]; pos+=12+ln
        if typ==b'IHDR':
            w,h,bd,ct,cm,fm,im=struct.unpack('>IIBBBBB',data)
        elif typ==b'IDAT': idat+=data
        elif typ==b'IEND': break
    bpp={0:1,2:3,3:1,4:2,6:4}[ct]*(bd//8)
    raw=zlib.decompress(idat); stride=w*bpp; rows=[]; prev=bytearray(stride); p=0
    for y in range(h):
        f=raw[p]; p+=1; cur=bytearray(raw[p:p+stride]); p+=stride
        for i in range(stride):
            a=cur[i-bpp] if i>=bpp else 0; b=prev[i]; c=prev[i-bpp] if i>=bpp else 0
            if f==1: cur[i]=(cur[i]+a)&255
            elif f==2: cur[i]=(cur[i]+b)&255
            elif f==3: cur[i]=(cur[i]+((a+b)>>1))&255
            elif f==4:
                pa=abs(b-c); pb=abs(a-c); pc=abs(a+b-2*c)
                pr=a if (pa<=pb and pa<=pc) else (b if pb<=pc else c)
                cur[i]=(cur[i]+pr)&255
        rows.append(cur); prev=cur
    return w,h,bpp,ct,rows
for path in sorted(glob.glob(os.path.join(sys.argv[1],'en-*.png'))):
    w,h,bpp,ct,rows=decode(path)
    def dark(r):
        ch=bpp if ct in (2,6) else 1
        n=0
        for x in range(0,w*bpp,bpp):
            v=min(r[x:x+min(3,bpp)]) if bpp>=3 else r[x]
            if v<200: n+=1
        return n
    darkrows=[y for y in range(h) if dark(rows[y])>0]
    # body region: skip header (first 6%) and footer (last 8%)
    body=[y for y in darkrows if 0.06*h<y<0.935*h]
    last=max(body) if body else None
    # largest blank vertical gap inside body
    gaps=[]; prevy=None
    for y in body:
        if prevy is not None and y-prevy>1: gaps.append((y-prevy,prevy,y))
        prevy=y
    gaps.sort(reverse=True)
    print(os.path.basename(path), f'{w}x{h}', 'last body ink row', last, f'= {last/h*100:.0f}% of page; blank to text-block bottom (92.6%): {(0.926*h-last)/h*100:.0f}% = {(0.926*h-last)/h*297:.0f} mm', 'biggest internal gap', gaps[0] if gaps else None)
