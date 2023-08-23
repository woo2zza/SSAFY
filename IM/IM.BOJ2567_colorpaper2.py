import sys
sys.stdin = open('input.txt','r')
paper = int(input())
arr = [['.'] * 102 for _ in range(102)]
lst = []
directy = [0,0,1,-1]
directx = [1,-1,0,0]
count = 0
def find(x, y):
    global  count
    for i in range(4):
        dx = x + directx[i]
        dy = y + directy[i]
        if dx >= 101 or dx < 0 or dy >= 101 or dy < 0: continue
        if arr[x][y] == 1:
            if arr[dx][dy] == '.':
                count += 1
    return count
for i in range(paper):
    # 색종이 갯수만큼 좌표 받기
    x, y = map(int, input().split())
    # 색종이 좌표에 숫자 1씩 더해준다
    for j in range(x,x+10):
        for k in range(y,y+10):
            arr[j][k] = 1

for i in range(102):
    for j in range(102):
        ret = find(i, j)

print(ret)
