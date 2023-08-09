arr = [
    ['_','_','_'],
    ['_','_','_'],
    ['A','T','K'],
    ['_','_','_'],
    ['_','_','_']
]
st1, st2 = [list(input().split()) for _ in range(7)]

directx = [1 ,-1, 0, 0]
directy = [0, 0, 1 ,-1]
def move(x, y):
    if st2 == 'UP':
        x += directx[1]
        x += directy[1]
    elif st2 == 'DOWN':
        x += directx[0]
        x += directy[1]
    elif st2 == 'RIGHT':
        y += directx[2]
        y += directy[2]
    elif st2 == 'LEFT':
        y += directx[3]
        y += directy[3]
    return x, y

for i in range(5):
    for j in range(3):
        if arr[i][j] == st1 and st1[1] == 'A':
            print(move(i,j))
        elif arr[i][j] == st1 and st1[1] == 'T':
            move(i,j)
        if arr[i][j] == st1 and st1[1] == 'K':
            move(i,j)

