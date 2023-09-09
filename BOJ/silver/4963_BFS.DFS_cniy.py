from collections import deque
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    used = [[0] * w for _ in range(h)]

    def bfs(y, x):
        dec = deque()
        dec.append((y, x))

        directy = [0,0,1,-1,1,-1,-1,1]
        directx = [1,-1,0,0,-1,1,-1,1]
        while dec:
            new = dec.popleft()
            ny, nx = new
            for i in range(8):
                dy, dx = ny + directy[i] , nx+directx[i]
                if dx < 0 or dy < 0 or dx > w-1 or dy > h-1:continue
                if used[dy][dx] == 1: continue
                if arr[dy][dx] == 1:
                    used[dy][dx] = 1
                    dec.append((dy,dx))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if used[i][j] == 0 and arr[i][j] == 1:
                used[i][j] = 1
                cnt += 1
                bfs(i, j)
    print(cnt)