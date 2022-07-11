for _ in range(int(input())):
    a = input()
    b = input()

    print(a)
    print(b)
    for i, j in zip(a, b):
        print( '.' if i==j else '*' , end="")
    
    print()