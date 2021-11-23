for _ in range(int(input())):
    cords = [*map(int, input().split(' '))]
    del cords[0]
    print(sum(cords) - len(cords)+1)