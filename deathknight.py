counter = 0
n = int(input())
for i in range(n):
    c = False
    for char in input():
        if char == "D" and c:
            counter += 1
        if char == "C":
            c = True
        else:
            c = False
print(n-counter)