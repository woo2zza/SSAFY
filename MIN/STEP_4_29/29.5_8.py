arr = [
    ['_','A','_'],
    ['#','_','D'],
    ['C','_','#'],
    ['#','_','_']
]
directy = [0, 1, 0, -1, 0]
directx = [1, 0, -1, 0, 1]

def find(i, j):
    for k in range(5):
        dy = i + directy[k]
        dx = j + directx[k]
        if dy < 0 or dx < 0 or dy >3 or dx > 2 : continue
        if  arr[dy][dx] == '_':
            arr[dy][dx] = arr[i][j]
            arr[i][j] = '_'

for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A' or arr[i][j] == 'D' or arr[i][j] == 'C':
            find(i, j)

for i in arr:
    print(*i)

