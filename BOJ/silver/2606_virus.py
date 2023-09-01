from collections import deque

C = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append(1)
cnt = -1
used = [0] * (C+1)
used[1] = 1

while q:
    new = q.popleft()
    cnt += 1
    for i in range(N):
        if arr[i][0] == new:
            if used[arr[i][1]] != 1:
                used[arr[i][1]] = 1
                q.append(arr[i][1])
        if arr[i][1] == new:
            if used[arr[i][0]] != 1:
                used[arr[i][0]] = 1
                q.append(arr[i][0])
print(cnt)