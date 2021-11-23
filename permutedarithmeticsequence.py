for c in range(int(input())):
    line = input().split(" ")
    line.pop(0)
    for a in range(len(line)):
        line[a] = int(line[a])
    diff = line[1] - line[0]
    for a in range(len(line)):
        if a == 0:
            continue
        if line[a] - line[a-1] != diff:
            break
    else:
        print("arithmetic")
        continue
    line.sort()
    diff = line[1] - line[0]
    for a in range(len(line)):
        if a == 0:
            continue
        if line[a] - line[a-1] != diff:
            break
    else:
        print("permuted arithmetic")
        continue
    print("non-arithmetic")