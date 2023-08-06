arr = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2]
]
directx = [-1,-1,1,1]
directy = [-1,1,-1,1]

def Sum(x, y):
    multi = 0
    for i in range(4):
        dx = x + directx[i]
        dy = y + directy[i]
        if dx > 4 or dx < 0 or dy > 4 or dy < 0 : continue
        multi += arr[dx][dy]

    return multi

Max = 0
idx = 0
idy = 0
for i in range(5):
    for j in range(5):
        ret = Sum(i, j)
        if ret > Max:
            Max = ret
            idx = i
            idy = j
print(idx, idy)
