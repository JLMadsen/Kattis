M,N,U,L,R,D=map(int,(input()+' '+input()).split())
e,p=enumerate,'#.'*(N+L+R)
ww=[input()for _ in range(M)]
o=[p[(g:=(i%2!=0)):L+g]+w+p[L+len(w)+g:]for i,w in e((['']*U)+ww+(['']*D))]
print('\n'.join([l[:N+L+R]for l in o]))