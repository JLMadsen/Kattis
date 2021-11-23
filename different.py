while(True):
    try:
        a, b = input().split(" ")
        a, b = int(a), int(b)
        if a > b:
            print(a-b)
        else:
            print(b-a)
    except:
        break