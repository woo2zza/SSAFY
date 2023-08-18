from collections import deque
arr=[[0,0,0,0,0,0],
     [1,0,0,0,1,0],
     [1,0,0,0,1,0],
     [0,0,0,0,0,0]]
directy=[0,0,-1,1]
directx=[1,-1,0,0]
# 생쥐 위치 (0,0), 치즈 위치(3,0), 친구 위치(3,4)
directy = [0 ,0, 1, -1]
directx = [1 ,-1, 0, 0]

def dfs(sty, stx, edy, dex):
    q = deque
    q.append((sty,stx, 0))
    # 큐 만들고 초기값으로 생쥐의 현 위치와 몇 걸음이동했는지 넣어주기
    while q:
        nowy, nowx , step = q.popleft()
        if nowy == edy and nowx == edx:
        for i in range(4):
            dy = sty + directy[i]
            dx = stx + directx[i]
            if dy > 3 or dy < 0 or dx > 3 or dx < 0 : continue
            if arr[dx][dy] == 1: continue


ret1 = bfs(0,0,3,0)
ret2 = bfs(3,0,3,4)