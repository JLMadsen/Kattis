for i in range(int(input())):
    _, s = int(input()), 0
    f = lambda r: sorted([*map(int, input().split())], reverse=r)
    print(f'case #{str(i+1)}:', sum([a*b for a,b in zip(f(0),f(1))]))