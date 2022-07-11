rooms, b = input().split(" ")
rooms, b = int(rooms), int(b)

if rooms == b:
    print("too late")
else:
    booked = []
    for f in range(b):
        booked.append(int(input()))
    for i in range(1,rooms+1):
        if i not in booked:
            print(i)
            exit()
