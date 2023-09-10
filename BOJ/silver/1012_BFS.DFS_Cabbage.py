from collections import deque
T = int(input())
for q in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for i in range(K):
        st, ed = map(int, input().split())
        arr[st][ed] =1 
        used = [[0] * N for _ in range(M)]

        directy = [0,0,-1,1]
        directx = [1,-1,0,0]


        def bfs(row, col):
            dec = deque()
            dec.append((row,col))
            while dec:
                new = dec.popleft()
                y,x = new
                for direc in range(4):
                    dy = y + directy[direc]
                    dx = x + directx[direc]
                    if dy<0 or dx<0 or dy>M-1 or dx>N-1:continue
                    if used[dy][dx] == 1: continue
                    if arr[dy][dx] == 1:
                        used[dy][dx] = 1
                        dec.append((dy,dx))
            

        cnt = 0
        for row in range(M):
            for col in range(N):
                if arr[row][col] == 1 and used[row][col] == 0:
                    used[row][col] = 1
                    ret = bfs(row, col)
                    cnt += 1

    print(cnt)
