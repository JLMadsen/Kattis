import re
n = int(input())
cups = []
for i in range(n):
    cups.append(input().split(" "))
new = []
for one, two in cups:
    if re.match('\d', one):
        one = int(one)/2
        new.append([two, one])
    else:
        two = int(two)
        new.append([one, two])
for i in range(len(new)):
    lowest = i
    for j in range(i, len(new)):
        if new[lowest][1] > new[j][1]:
            lowest = j
    new[i], new[lowest] = new[lowest], new[i]
for n in new:
    print(n[0])