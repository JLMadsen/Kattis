from sys import stdin, stdout
from collections import deque

front = deque()
back  = deque()

for _ in range(int(stdin.readline())):
    op, num = stdin.readline().split()
    num = int(num)

    if op[0] == 'g':
        if num < len(front):
            stdout.write( str(front[num]) + '\n' )
        else:
            stdout.write( str(back[ num - len(front) ]) + '\n' )
    
    elif op[5] == 'm':
        if len(back) > len(front):
            front.append( back.popleft() )
        back.appendleft(num)

    elif op[5] == 'f':
        front.appendleft(num)

        # hvis front er lenger enn back
        # flytt 1 item over
        if len(front) > len(back) :
            back.appendleft( front.pop() )

    elif op[5] == 'b':
        back.append(num)

        if len(back) > len(front) :
            front.append( back.popleft() )