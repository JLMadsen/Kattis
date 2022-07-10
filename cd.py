
N, M = [*map(int, input().split(' '))]
while N and M:
    
    jack = {}
    for _ in range(N):
        jack[int(input())] = 1
    
    jill = {}
    for _ in range(M):
        jill[int(input())] = 1
        
    sell = 0
    for cd in jack.keys():
        if cd in jill:
            sell += 1
            
    print(cell)
    N, M = [*map(int, input().split(' '))]