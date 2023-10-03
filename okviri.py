t,l,e = input(),['' for _  in range(5)], enumerate
a=lambda h: [l[j]+c for j,c in e(h)]
y=0
for i, d in e(t,1):
    p='*' if (w:=i>0 and i%3==0) else '#'
    if not y:
        l = [c[:-1] for c in l]
        l = a(f'..{p}..')
    for s in [f'.{p}.{p}.',f'{p}.{d}.{p}',f'.{p}.{p}.',f'..{p}..']:
        l = a(s)
    y=w
print('\n'.join(l))