import sys
sys.stdin = open('SSAFY/SWEA/input.txt','r')
from collections import deque

for test_case in range(1,11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    idx = 0
    for i in range(100):
        if arr[99][i] ==2:
            idx = i
    directy = [0,0,-1]
    directx = [-1,1,0]
    q = deque()
    q.append((99 , idx))
    Flag = 1
    while Flag:
        nowy , nowx = q.popleft()
        
        for i in range(3):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dx > 99 or dx < 0 or dy > 99 or dy < 0 : continue

            if arr[dy][dx] == 0: continue
            arr[nowy][nowx] = 0 

            if arr[dy][dx] == 1 and dy==0:
                ret =  dx
                Flag = 0
                break
            q.append((dy, dx))

            if arr[dy][dx] == 1:
                break 
    print(f'#{test_case} {ret}')

    # abc(0  x 좌표)    넘겼을 때 0 이면 +1
# 0번이 1이면 direct 아래 오른쪽 왼쪽받아주고 1이라면 step + 1