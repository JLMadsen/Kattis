words = {}
while 1:
    try:
        a, b = input().split()
    except:
        break
    words[b] = a
while 1:
    word = ''
    try:
        word = input()
    except EOFError:
        break
    if not word:
        break
    if word not in words:
        print('eh')
    else:
        print(words[word])