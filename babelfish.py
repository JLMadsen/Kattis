from sys import stdin
words = {}
for line in stdin:
    line = line.rstrip()
    arr = line.split(' ')
    if len(arr) == 2:
        words[arr[1]] = arr[0]
    else:
        if not line:
            continue
        if line in words.keys():
            print(words[line])
        else:
            print('eh')