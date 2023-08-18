from collections import deque
arr=[[0,0,0,0,0,0],
     [1,0,0,0,1,0],
     [1,0,0,0,1,0],
     [0,0,0,0,0,0]]
directy=[0,0,-1,1]
directx=[1,-1,0,0]
# 생쥐의 위치 -> 치즈위치  +  치즈위치 -> 친구의 위치

def bfs(sty, stx, edy, edx):
    used = [[0]*6 for _ in range(4)]
    used[sty][stx] = 1
    q = deque()
    q.append((sty, stx, 0))
    while q:
        nowy, nowx, step = q.popleft()
        if edy == nowy and edx == nowx:
            return step
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy > 3 or dy < 0 or dx > 5 or dx < 0 :
                continue
            if used[dy][dx] == 1:
                continue
            if arr[dy][dx] ==1:
                continue
            used[dy][dx] = 1
            q.append((dy, dx, step + 1))

ret1 = bfs(0,0,3,0)
ret2 = bfs(3,0,3,4)
print(ret1 + ret2)