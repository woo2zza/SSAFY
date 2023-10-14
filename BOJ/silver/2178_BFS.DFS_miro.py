import sys  
sys.stdin = open('SSAFY/BOJ/silver/input.txt')
from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]

def Map(i,j):
    deq = deque()
    deq.append((i,j))

    while deq:
        now = deq.popleft()
        sy, sx = now

    
        for q in range(4):
            dy = sy + directy[q]
            dx = sx + directx[q]
            if dx > M-1 or dx < 0 or dy < 0 or dy > N-1 :continue
            if lst[dy][dx] == '0': continue
            if lst[dy][dx] == '1':
                lst[dy][dx] = int(lst[sy][sx]) +1
                deq.append((dy,dx))

    return lst[N-1][M-1]

ret = Map(0,0)
print(ret)