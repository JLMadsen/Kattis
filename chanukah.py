for _ in range(int(input())):
    dataNr, days = input().split(' ')
    candles = 0
    for i in range(1, int(days)+1):
        candles += i+1
    print(dataNr, candles)