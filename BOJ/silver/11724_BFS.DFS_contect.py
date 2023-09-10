from collections import deque
N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    st, ed = map(int, input().split())
    arr[st][ed] = 1
    arr[ed][st] = 1

used = [[0]*(N+1) for _ in range(N+1)]

def bfs(i,j):
        dec = deque()
        dec.append((i,j))
        while dec:
            new = dec.popleft()
            x, y = new
            for col in range(1, N+1):
                if arr[y][col] == 1 and used[y][col] == 0:
                    used[y][col] = 1
                    used[col][y] = 1
                    dec.append((y,col))

cnt = 0
for i in range(1,N +1):
    for j in range(1,N+1):
        if arr[i][j] == 1 and used[i][j] == 0:
            used[i][j] = 1
            used[j][i] = 1
            cnt += 1
            bfs(i,j)

print(cnt)