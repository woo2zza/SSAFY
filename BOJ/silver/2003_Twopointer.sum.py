from collections import deque   
N, M = map(int, input().split())
lst = list(map(int, input().split()))
dec = deque()
dec.append(lst[0])
cnt = 0
if dec[0] == M:
    cnt += 1
    dec.popleft()

for i in range(1, N):
    dec.append(lst[i])
    if sum(dec) > M:
        dec.popleft()
    
    if sum(dec) == M:
        dec.popleft()
        cnt += 1

print(cnt)