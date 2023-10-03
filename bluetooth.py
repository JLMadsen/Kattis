import sys
m,d=[[8,8],[8,8]],sys.stdin;next(d)
for(i)in d:m['+'in i][i[0].isdigit()]-=9**(i[3]=='b')
[a,b],[c,d]=m;print([a>0<c,d>0<b,1].index(1))