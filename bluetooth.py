import sys
m,d=[[8,8],[8,8]],sys.stdin;next(d)
for(a,b,_,c,_)in d:a,b=[a,b][::1-2*(l:=a not in'+-')];m[a=='+'][l]-=1*c=='m'or 9
[a,b],[c,d]=m;print([a>0<c,d>0<b,1].index(1))