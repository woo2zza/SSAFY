import sys
from collections import deque
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
            break
        else:
            if 0 <= now-1 < Max and  direct[now-1] == 0 :
                direct[now-1] = direct[now]+1
                deq.append(now-1)

            elif 0 <= now+1 < Max and direct[now+1] == 0 :
                direct[now-1] = direct[now]+1
                deq.append(now+1)

            elif 0 <= now*2 < Max and direct[now*2] == 0 :
                direct[now-1] = direct[now]
                deq.append(now*2)

bfs(N)