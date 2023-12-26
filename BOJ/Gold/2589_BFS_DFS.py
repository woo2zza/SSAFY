# 육지는 L , 바다는 W
# 상하좌우로 이웃한 육지로 이동가능, 한 칸 이동시 + 한시간
# 시간이 가장 오래걸리는 보물 사이의 최단거리?

# 설계
# 1. 전체 배열 중 L을 찾고 BFS로 L주변을 탐색
# 2. direct배열을 이용해 경계선 + 주변의 L찾기
# 3. 한번 지난길은 다시 가지 못하게 used 배열 사용
# 4. 한번 지나갈때마다 cnt를 +1하고 더 이상 움직일 수 없을때 cnt를 return
# 5. return을 하면 전체 배열 중 다음 L을 찾고 used를 초기화
# 6. return받은 cnt를 배열에 담고 배열 중 최댓값 구하기

from collections import deque

Y, X = map(int, input().split())
arr = list((input()) for _ in range(Y))

count = []

directy = [0,0,1,-1]
directx = [1,-1,0,0]

def bfs(i, j):
    deq = deque()
    cnt = 0
    max = -2e33
    deq.append((i,j, cnt))
    used = [[0]*X for _ in range(Y)]
    used[i][j] = 1
    while deq:

        i, j, cnt = deq.popleft()
        for q in range(4):
            newi = directy[q] + i
            newj = directx[q] + j
            if newi < 0 or newi > Y-1 or newj < 0 or newj > X-1:continue
            if used[newi][newj] != 0: continue
            if arr[newi][newj] == 'L':
                used[newi][newj] = cnt +1
                deq.append((newi, newj, cnt+1))
    for a in range(Y):
        for b in range(X):
            if used[a][b] > max:
                max = used[a][b]
    return max

for i in range(Y):
    for j in range(X):
        if arr[i][j] == "L":
            count.append(bfs(i, j))
print((count))