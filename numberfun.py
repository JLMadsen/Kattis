def yes():
    print('Possible')
def no():
    print('Impossible')

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if a + b == c:
        yes()
    
    elif a-b == c:
        yes()

    elif b-a == c:
        yes()

    elif a*b == c:
        yes()

    elif a/b == c:
        yes()

    elif b/a == c:
        yes()

    else:
        no()