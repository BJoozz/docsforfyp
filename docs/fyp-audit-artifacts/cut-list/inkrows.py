import sys, zlib, struct, glob, os
def load(path):
    d=open(path,'rb').read(); i=8; idat=b''; w=h=0
    while i<len(d):
        l=struct.unpack('>I',d[i:i+4])[0]; t=d[i+4:i+8]; c=d[i+8:i+8+l]
        if t==b'IHDR': w,h,bd,ct,_,_,il=struct.unpack('>IIBBBBB',c)
        elif t==b'IDAT': idat+=c
        elif t==b'IEND': break
        i+=12+l
    bpp={0:1,2:3,4:2,6:4}[ct]; raw=zlib.decompress(idat); stride=w*bpp
    rows=[]; prev=bytearray(stride); p=0
    for y in range(h):
        f=raw[p]; p+=1; line=bytearray(raw[p:p+stride]); p+=stride
        for x in range(stride):
            a=line[x-bpp] if x>=bpp else 0; b=prev[x]; c=prev[x-bpp] if x>=bpp else 0
            if f==1: line[x]=(line[x]+a)&255
            elif f==2: line[x]=(line[x]+b)&255
            elif f==3: line[x]=(line[x]+((a+b)>>1))&255
            elif f==4:
                pa=abs(b-c); pb=abs(a-c); pc=abs(a+b-2*c)
                pr=a if (pa<=pb and pa<=pc) else (b if pb<=pc else c)
                line[x]=(line[x]+pr)&255
        rows.append(bytes(line)); prev=line
    return w,h,bpp,rows
for path in sys.argv[1:]:
    w,h,bpp,rows=load(path)
    ink=[]
    for y,r in enumerate(rows):
        dark=0
        for x in range(0,w*bpp,bpp):
            if r[x]<160: dark+=1
        ink.append(dark)
    # body region: below header rule (~y>50) and above footer (~y<870)
    body=[y for y in range(55,int(h*0.925)) if ink[y]>0]
    last=max(body) if body else None
    mm=lambda px: px*25.4/80
    print(os.path.basename(path), w,h, 'last ink row', last, f'= {last/h*100:.1f}% of height', f'blank to text bottom(866px): {mm(866-last):.1f} mm')
