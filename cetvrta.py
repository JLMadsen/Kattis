from collections import Counter

x = []
y = []

for i in range(3):
    thing = input().split(" ")
    x.append(thing[0])
    y.append(thing[1])

cnt1 = Counter(x)
cnt2 = Counter(y)

xFound = 0
yFound = 0

for pos, value in cnt1.items():
	if value == 1:
		xFound = pos

for pos, value in cnt2.items():
	if value == 1:
		yFound = pos

print(xFound, yFound)