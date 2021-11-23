n, g = input().split(" ")
n, g = int(n), int(g)
obs = []
for f in range(g):
    ne = int(input())
    if ne not in obs:
        obs.append(ne)
for j in range(n):
    if j not in obs:
        print(j)
print("Mario got "+str(len(obs))+" of the dangerous obstacles.")