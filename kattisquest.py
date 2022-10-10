from collections import defaultdict
import sys
import time

input = sys.stdin.readline

n = int(input())
pool = defaultdict(lambda: [])
keys = []

def session(x):
    global pool
    gold = 0
    energy = x
    sorted_keys = sorted(keys, reverse=1)
    m = len(sorted_keys)
    idx = 0
    while idx < m:
        key = sorted_keys[idx]
        if key <= energy:
            if not pool[key]:
                idx += 1
                keys.remove(key)
                continue
            high = max(pool[key])
            gold += high
            energy -= key
            pool[key].remove(high)
        else:
            idx += 1
    return gold

t0 = time.time()
for _ in range(n):
    action = input().split()
    if action[0].startswith('add'):
        energy = int(action[1])
        if energy not in keys: keys.append(energy)
        pool[energy].append(int(action[2]))
    else:
        print( session(int(action[1])) )

t1 = time.time()
print('tid', ("%.5f" % (t1-t0,)))
