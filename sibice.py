import math
N, W, H = map(int, input().split())
c = math.sqrt(W**2 + H**2)
for _ in range(N):
    length = int(input())
    if length <= c:
        print('DA')
    else:
        print('NE')