WIDTH = 8
pos_to_index    = lambda x: ord(x) - ord('A') if not x.isnumeric() else (int(x) - 1)
index_to_letter = lambda x: chr(x + ord('A'))
is_odd          = lambda x: x % 2 == 0
is_white        = lambda x, y: is_odd(x + y)
def goto(pos, mod):
    next = []
    for i in range(WIDTH):
        a = pos[0] + (mod[0] * (i+1))
        b = pos[1] + (mod[1] * (i+1))
        if a < 0 or b < 0:
            return next
        if a == (WIDTH) or b == (WIDTH):
            return next
        
        next.append((a, b))
    return next
def print_path(*steps):
    print(len(steps) - 1, end=" ")
    for step in steps:
        print(index_to_letter(step[0]), step[1]+1, end=" ")
    print()
for _ in range(int(input())):
    s1, s2, e1, e2 = map(pos_to_index, input().split())
    start, goal = (s1, s2), (e1, e2)
    if is_white(*start) != is_white(*goal):
        print('Impossible')
        continue
    if goal == start:
        print_path(start)
        continue
    found = False
    for mod1 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        for step in goto(start, mod1):
            if step == goal:
                print_path(start, goal)
                found = True
                break
            for mod2 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                if goal in goto(step, mod2):
                    found = True
                    print_path(start, step, goal)
                    break
            if found:
                break
        if found:
            break