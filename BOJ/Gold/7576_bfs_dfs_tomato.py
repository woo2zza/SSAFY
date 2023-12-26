# M * N 의 상자 (M+1 , N+1 로 놔야 칸 안에 넣을 수 있음)
# 하루가 지나면
# 익은 토마토 주변에 익지 않은 토마토가 있으면 익지않은 토마토도 익음 (direct)
# 며칠이 지나야 모든 토마토가 익는지?

# 설계
# 1. (M+1) * (N+1) 의 격자를 만든다
# 2. direct를 통해 경계선을 만든다
# 3. bfs를 통해 (0,0)부터 토마토의 유무를 파악 후 토마토가 있으면 주변 토마토가 있는지 확인
# 4. 토마토가 있다면 count +1을 해주고 해당 토마토로 이동.
#    없으면 다음 격자칸으로 이동
from collections import deque
import sys
sys.stdin = open("input.txt","r")

A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(B)]

directy = [0,0,1,-1]
directx = [1,-1,0,0]

cnt = 0

def bfs():
    q = deque()
    for i in range(B):
        for j in range(A):
            if arr[i][j] == 1:
                q.append([i,j])

    while q:
        now = q.popleft()
        ty, tx = now
        for w in range(4):
            newy = directy[w] + ty
            newx = directx[w] + tx
            if newy < 0 or newy > B-1 or newx < 0 or newx > A-1:continue
            if arr[newy][newx] == 0:
                arr[newy][newx] = arr[ty][tx] +1
                q.append([newy, newx])

bfs()
Flag = False
for i in range(B):
    for j in range(A):
        if arr[i][j] == 0:
            Flag = True
            break
if Flag: print(-1)
else:
    print(max(map(max,arr))-1)