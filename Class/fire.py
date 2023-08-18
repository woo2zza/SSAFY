from collections import deque

N = int(input())  # 맵 크기
arr = [list(input()) for _ in range(N)]
a, b = map(int, input().split()) # 민철 좌표

arr[a][b] = 1  # 민철 위치를 1로 표시
used = [[0]*N for _ in range(N)]
directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

def find(st, ed, i, j):
    count = 0
    de = deque()
    de.append((a, b, count))
    my, mx, count = de.popleft()

    for q in range(4):
        dy = a + directy[q]
        dx = b + directx[q]
        if dy > N-1 or dy < 0 or dx > N-1 or dx < 0 or arr[dx][dy] == '#': continue
        if used[dy][dx] == 1: continue
        used[dy][dx] = 1



idx = 0
idy = 0
# 소화기 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            idx = i
            idy = j
            find(a, b, i, j)


