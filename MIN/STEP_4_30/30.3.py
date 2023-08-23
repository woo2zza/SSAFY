from collections import deque
arr=[
    [0 ,1 ,0 ,0 ,1 ,0],
    [0 ,0 ,1 ,0 ,0 ,1],
    [0 ,0 ,0 ,1 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0]
]

k = int(input())
q = deque()
q.append(k)


while q:
    now = q.popleft()
    print(now, end = ' ')
    for i in range(6):
        if arr[now][i] ==1:
            q.append(i)
