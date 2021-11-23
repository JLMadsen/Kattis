for i in range(int(input())):
    n = int(input())
    peeps = input().split(" ")
    
    for peep in peeps:
        count = 0
        for p in peeps:
            if peep == p:
                count += 1
        if count == 1:
            print("Case #"+ str((i+1)) +": "+ peep)