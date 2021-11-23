# last in, first out
def isStack(pairs):
    stack = []
    for pair in pairs:
        if(pair[0] == 1):
            stack.append(pair[1])
        elif(stack.pop() != pair[1]):
                return False
    return True
# first in, first out
def isQueue(pairs):
    queue = []
    for pair in pairs:
        if(pair[0] == 1):
            queue.append(pair[1])
        elif(queue.pop(0) != pair[1]):
                return False
    return True

#largest first
def isPQueue(pairs):
    pqueue = []
    for pair in pairs:
        if(pair[0] == 1):
            pqueue.append(pair[1])
        else:
            high, ind = 0,0
            for plc, val in enumerate(pqueue):
                if val > high:
                    high, ind = val, plc
            if(pqueue.pop(ind) != pair[1]):
                return False
    return True
while 1:
    try:
        n = int(input())
    except:
        exit()
    pairs = []
    for i in range(n):
        a, b = input().split(' ')
        a, b = int(a), int(b)
        pairs.append([a, b])
    try:
        s = isStack(pairs)
        q = isQueue(pairs)
        p = isPQueue(pairs)
    except:
        print("impossible")
        continue
    boolSum = s+q+p 
    if boolSum < 1 :
        print("impossible")
        continue
    if boolSum > 1 :
        print("not sure")
        continue
    if s :
        print("stack")
        continue
    if q :
        print("queue")
        continue
    if p :
        print("priority queue")
        continue