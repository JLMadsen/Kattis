import math
a,b,c,d=map(int,input().split())
s=sum([a,b,c,d])/2
print(math.sqrt( (s-a)*(s-b)*(s-c)*(s-d) ))