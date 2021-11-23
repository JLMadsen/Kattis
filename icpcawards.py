n = int(input())
teams = []
for i in range(n):
    teams.append(input().split(" "))
unis = []
result = []
for team in teams:
    if team[0] in unis:
        continue
    else:
        unis.append(team[0])
        result.append(team[0] +" "+ team[1])
for i in range(12):
    print(result[i])