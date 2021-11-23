cases = []
while(True):
    try:
        cases.append(input())
    except:
        break
for case in cases:
    res = 0
    for num in case.split(" "):
        res += int(num)
    print(int(res/2))