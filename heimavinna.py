tasks = input()
ranges = tasks.split(';')
counter = 0
for r in ranges:
    a, b = [*map(lambda x: int(x), r.split('-'))] if '-' in r else [0, 0]
    counter += len([*range(a, b+1)])
print(counter)