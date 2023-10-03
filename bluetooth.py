import sys
m,d=[8]*4,[*sys.stdin]
for(i)in d[1:]:m[2*('+'in i)+(i[1]in'+-')]-=9**('b'in i)
a,b,c,d=m;print([a>0<c,d>0<b,1].index(1))