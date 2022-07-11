bdays = {}

for _ in range(int(input())):

    name, score, day = input().split()
    score = int(score)

    if day not in bdays.keys():
        bdays[day] = [name, score]

    else:
        comparison = bdays[day]
        if score > comparison[1]:
            bdays[day] = [name, score]

print(len(bdays))
[print(person[0]) for person in sorted(bdays.values()) ]