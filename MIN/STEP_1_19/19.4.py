arr = [['_']*5 for _ in range(4)]

directx = [-1,-1,-1,0,0,1,1,1]
directy = [-1,0,1,-1,1,-1,0,1]
def boom(x, y):
    for i in range(8):
        dx = x + directx[i]
        dy = y + directy[i]
        if dx > 3 or dy > 4 or dx <0 or dy < 0 : continue
        arr[dx][dy] = '#'
    
for i in range(2):
    x, y = map(int, input().split())
    boom(x, y)
for i in arr:
    print(*i)