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
    if is_white(s1, s2) != is_white(e1, e2):
        print('Impossible')
        continue
    steps = 0
    start = (s1, s2)
    goal = (e1, e2)
    queue = []
    if goal == start:
        print_path(start)
        continue
    found = False
    middle = ()
    for mod1 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        next = goto(start, mod1)
        for step in next:
            if step == goal:
                print_path(start, goal)
                found = True
                break
            for mod2 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                next2 = goto(step, mod2)
                if goal in next2:
                    found = True
                    print_path(start, step, goal)
                    break
            if found:
                break
        if found:
                break