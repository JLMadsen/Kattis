peeps = []
for i in range(int(input())):
    peeps.append(input())
    
temp = sorted(peeps)

if temp == peeps:
    print("INCREASING")
    exit()

temp = sorted(peeps, reverse=True)

if temp == peeps:
    print("DECREASING")
    exit()
    
print("NEITHER")