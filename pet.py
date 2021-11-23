from collections import Counter
score = {}
for j in range(5):
    score[(j+1)] = 0
    points = input().split(" ")
    for point in points:
        score[(j+1)] += int(point)
score = Counter(score)      
winner = score.most_common(1)
print(winner[0][0], winner[0][1])