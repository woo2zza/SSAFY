from collections import deque

arr=[
    [0 ,0 ,0 ,0, 1 ,0],
    [1 ,0 ,1 ,0 ,0 ,1],
    [1 ,0 ,0 ,1 ,0 ,0],
    [1 ,1 ,0 ,0 ,0 ,0],
    [0 ,1 ,0, 1,0, 1],
    [0, 0, 1, 1 ,0,0]
]
used = [0] * 6
num = int(input())

def bfs(num):
    q = deque()
    q.append(num)

    while q:
        now = q.popleft()
        print(now)
        for i in range(6):
            if used[i] == 1: continue
            if arr[now][i] == 1:
                used[i] = 1
                q.append(i)
used[num] =1
bfs(num)

