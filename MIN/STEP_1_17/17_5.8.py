map1 = [
    [3, 55, 42],
    [-5, -9, -10]
]
def find(pix):
    Flag = False
    for i in range(2):
        for j in range(3):
            if map1[i][j] == pix:
                Flag = True
    return Flag


pix = [list(map(int, input().split())) for _ in range(2)]
for i in range(2):
    for j in range(2):
        ret = find(pix[i][j])
        if ret : print('Y', end = ' ')
        else : print('N', end = ' ')
    print()