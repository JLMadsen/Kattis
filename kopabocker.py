from heapq import *
i=lambda:map(int, input().split())
n,m= i()
r = 0
shops = []
heapify(shops)
for _ in range(m):
p,b=i()
heappush(shops,(p,b))
while 1:
p,b=heappop(shops)
if b>n:
    print('>', r)
    break
r+=p*b
n-=b
