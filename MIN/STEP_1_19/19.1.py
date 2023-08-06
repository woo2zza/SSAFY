arr = [
    [3 ,5 ,4],
    [1, 1 ,2],
    [1 ,3 ,9]
]
x, y = map(int, input().split())

directx = [-1,1,0,0]
directy = [0,0,1,-1]
Sum = 0
for i in range(4):
    dx = x + directx[i]
    dy = y + directy[i]
    if dx > 2 or dx < 0 or dy > 2 or dy < 0: continue
    Sum += arr[dx][dy]
print(Sum)