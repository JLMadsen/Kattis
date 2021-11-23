valid = [1, 1, 2, 2, 2, 8]
result = ''
for val, inp in zip(valid, input().split(' ')):
    r = val - int(inp)
    result += str(r) + ' '
print(result)