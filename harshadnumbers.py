num = int(input())
def is_harshad(n):
    h = sum([*map(int, [*str(n)])])
    return not n%h
while not is_harshad(num):
    num += 1
print(num)