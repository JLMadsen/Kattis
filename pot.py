n = int(input())
sum = 0

for j in range(n):
    p = input()
    pow = int(p[-1])
    num = ""
    for i in range( (len(p)-1) ):
        num += p[i]
    num = int(num)
    sum += num**pow
    
print(sum)