import sys
sys.stdin = open("input.txt","r")
new = [
    [1 ,1, 1 ,1 ,1 ,1],
    [1 ,1, 1 ,1 ,1 ,1],
    [1, 1, 1, 1 ,1, 1],
]

arr=[
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S']
]

directy = [0, 0, 1 ,-1, 0]
directx = [1, -1, 0 ,0 ,0]

def find(i, j):
    for w in range(5):
        dy = i + directy[w]
        dx = j + directx[w]
        if dx < 0 or dy < 0 or dx >5 or dy >2 : continue
        if new[dy][dx] == 0:
            new[dy][dx] = 1
        else:
            new[dy][dx] = 0
    return new

st = list(input())
for q in range(len(st)):
    for i in range(3):
        for j in range(6):
            if arr[i][j] == st[q]:
                ret =find(i,j)


for i in range(3):
    for j in range(6):
        if new[i][j] == 0:
            arr[i][j] = '#'
for i in arr:
    print(*i, sep= '')