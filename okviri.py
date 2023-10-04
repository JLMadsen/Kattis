t,l,e=input(),['']*5,enumerate;a=lambda h:[l[j]+c for j,c in e(h)];y=0
for i,d in e(t,1):
    p='*'if(w:=i>0 and i%3==0)else'#';s,m=f'..{p}..',f'.{p}.{p}.'
    if not y:l=[c[:-1]for c in l];l=a(s)
    for s in[m,f'{p}.{d}.{p}',m,s]:l=a(s);y=w
print('\n'.join(l))

