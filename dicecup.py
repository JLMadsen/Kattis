n, m = map(int, input().split())
sums = {}
for i in range((n if n>m else m)*2 + 2):
    sums[i] = 0
for i in range(n):
    for j in range(m):
        sums[ (i+1)+(j+1) ] += 1
highest = max(sums.values())
for k, v in sums.items():
    if v == highest:
        print(k)