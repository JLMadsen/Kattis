R, C, ZR, ZC = map(int, input().split())
figure = [input() for i in range(R)]
new_figure = [[',' for j in range( C * ZC )] for l in range( R * ZR )]
for r, line in enumerate(figure):
    for rm in range(ZR):
        for c, char in enumerate(line):
            for cm in range(ZC):
                try:
                    new_figure[ (r*ZR) + rm ][ (c*ZC) + cm ] = figure[r][c]
                except:
                    pass
for line in new_figure:
    print(''.join(line))