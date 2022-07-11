W = int(input())
N = int(input())
L = 0

pieces = [[*map(lambda x: int(x), input().split(' '))] for _ in range(N)]
pieces = [a*b for a, b in pieces]
print(sum(pieces)//W)
#print((sum([*zip(*pieces)][1])*sum(next(zip(*pieces))))/W)