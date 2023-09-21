from collections import deque
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    st, ed = map(int, input().split())
    arr[st].append(ed)
    arr[ed].append(st)
for i in arr:
    i.sort()
used_dfs = [0] * (N+1)
used_bfs = [0] * (N+1)
def dfs(now):
    print(now, end = ' ')
    for i in arr[now]:
        if used_dfs[i] == 1: continue
        used_dfs[i] = 1
        dfs(i)

def bfs(now):
    deq = deque()
    deq.append(now)
    while deq:
        new = deq.popleft()
        print(new, end = ' ')
        for i in arr[new]:
            if used_bfs[i] == 1: continue
            deq.append(i)
            used_bfs[i] = 1

used_dfs[V] = 1
used_bfs[V] = 1
dfs(V)
print()
bfs(V)
