from collections import deque
import sys
sys.stdin = open("input.txt","r")
N, K = map(int, input().split())
Max = 100001
direct = [0] * (Max +1)
def bfs(N):
    deq = deque()
    deq.append(N)

    while deq:
        now = deq.popleft()
        if now == K:
            print(direct[now])
            print(direct)
            break
        for next in (now-1, now+1, now*2):
            if next < 0 or next > Max or direct[next] != 0 : continue
            direct[next] = direct[now] +1
            deq.append(next)

bfs(N)