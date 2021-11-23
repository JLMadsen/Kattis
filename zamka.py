l = int(input())
d = int(input())
x = int(input())
for n in range(l, d + 1):
    if sum( [int(c) for c in str(n)] ) == x:
        print(n)
        break
for m in reversed(range(l, d + 1)):
    if sum( [int(c) for c in str(m)] ) == x:
        print(m)
        break