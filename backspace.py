out = []
for c in input():
    if c == '<':
        out.pop()
    else:
        out.append(c)
print(''.join(out))