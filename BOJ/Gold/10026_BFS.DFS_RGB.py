import sys
from collections import deque
sys.stdin = open("input.txt","r")
N = int(input())
lst = [list(input()) for _ in range(N)]
used = [[0]*N for _ in range(N)]
cnt1 = 0
cnt2 = 0

directy = [0 ,0, 1, -1]
directx = [1, -1, 0, 0]

def bfs(x, y):
    deq = deque()
    deq.append((x,y))
    while deq:
        now = deq.popleft()
        new_x, new_y = now

        for i in range(4):
            dx = new_x + directx[i]
            dy = new_y + directy[i]
            if dx>N-1 or dx<0 or dy>N-1 or dy<0 : continue
            if used[dx][dy] == 1: continue
            if lst[dx][dy] != lst[new_x][new_y]: continue
            used[dx][dy] = 1
            deq.append((dx,dy))

for j in range(N):
    for k in range(N):
        if used[j][k] == 1: continue
        used[j][k] = 1
        bfs(j, k)
        cnt1+=1

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'G':
            lst[i][j] = 'R'

used = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if used[i][j] == 1: continue
        bfs(i,j)
        cnt2 += 1
print(cnt1, cnt2)