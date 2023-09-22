from collections import deque
import sys
sys.stdin = open("input.txt","r")
N, K = map(int, input().split())
Max = 100001
direct = [0] * (Max +1)
cnt = 0
def bfs(N):
    global cnt
    deq = deque()
    deq.append(N)

    while deq:
        now = deq.popleft()
        if now == K:
            cnt += 1
            result = direct[now]

        for next in (now*2, now-1, now+1 ):
            if next < 0 or next > Max  or direct[next] != 0 : continue
            direct[next] = direct[now] +1
            deq.append(next)

    return f'{result}\n{cnt}'
ret = bfs(N)
print(ret)


