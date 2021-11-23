for _ in range(int(input())):
    input()
    candies = [int(input()) for _ in range(int(input()))]
    print('YES' if not sum(candies)%len(candies) else 'NO')