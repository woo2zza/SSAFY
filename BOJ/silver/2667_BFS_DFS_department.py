import sys
sys.stdin = open('woo2zza/SSAFY/Boj/silver/input.txt','r')
def input(): return sys.stdin.readline().rstrip()   
from collections import deque


N = int(input())
lst = [list(input())  for _ in range(N)]
used = [[0]*N for _ in range(N)]

directy = [0,0,-1,1]
directx = [1,-1,0,0]

cnt = 0
def Map(i, j):
    global cnt
    deq = deque()
    deq.append((i, j))

    for q in range(4):
        dy = i + directy[q]
        dx = j + directx[q]
        if dx < 0 or dx > N-1 or dy < 0 or dy > N-1:continue
        if used[dy][dx] == 1: continue
        if lst[dy][dx] == 1:
            used[dy][dx] = 1
            deq.append((dy,dx))
            cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if used[i][j] == 1: continue
        if lst[i][j] == 1:
            used[i][j] = 1
            ret = Map(i, j)
            print(ret)

