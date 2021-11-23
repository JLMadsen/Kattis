N, B = input().split(' ')
hands = [input() for _  in range(int(N)*4)]
scores = {
    'A': [11, 11],
    'K': [4, 4],
    'Q': [3, 3],
    'J': [20, 2],
    'T': [10, 10],
    '9': [14, 0],
    '8': [0, 0],
    '7': [0, 0]
}
sum = 0
for a, b in hands:
    sum += scores[a][b!=B*1]
print(sum)