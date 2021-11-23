n, m = input().split(" ")
n, m = int(n), int (m)
out = 0
denied = 0
for i in range(m):
    action, amount = input().split(" ")
    amount = int(amount)
    if action == "enter":
        if amount + out > n:
            denied += 1
        else:
            out += amount
    else:
        out -= amount
print(denied)