n = int(input())

in_da_house = []

for i in range(n):
    action, name = input().split(" ")
    
    if action == "entry":
        if name in in_da_house:
            print(name, "entered (ANOMALY)")
        else:
            in_da_house.append(name)
            print(name, "entered")
    if action == "exit":
        if name not in in_da_house:
            print(name, "exited (ANOMALY)")
        else:
            in_da_house.pop(in_da_house.index(name))
            print(name, "exited")