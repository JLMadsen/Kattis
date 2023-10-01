mouth = [[36,36],[36,36]]
for (a, b, _, c) in [input() for _ in range(int(input()))]:
    a, b = (b, a) if (left := a not in '+-') else (a, b)
    mouth[(a == '+')*1][left] -= int(b) if c == 'm' else 99
print(0 if mouth[0][0] > 0 and mouth[1][0] > 0 else (1 if mouth[0][1] > 0 and mouth[1][1] > 0 else 2))