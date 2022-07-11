for n in range(int(input())):

    b, p = input().split(' ')
    b = int(b)
    p = float(p)

    bpm = 60 * b / p
    abpm = 60 / p

    print(bpm-abpm, bpm, bpm+abpm)