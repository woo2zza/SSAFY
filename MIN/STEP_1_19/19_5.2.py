arr = [list(map(int, input().split())) for _ in range(5)]
diretx = [-1,-1,-1,0,0,1,1,1]
direty = [-1,0,1,-1,1,-1,0,1]

def find(x, y):
    for i in range(8):
        dx = x + diretx[i]
        dy = y + direty[i]
        if dx>4 or dx < 0 or dy>3 or dy<0: continue
        if arr[dx][dy] == 1:
            return 1
    return 0

ret_arr = []
for i in range(5):
    for j in range(4):
        if arr[i][j] == 1:
            ret = find(i,j)
            ret_arr.append(ret)
if 1 in ret_arr:
    print('불안정한 상태')
else: print('안정된 상태')