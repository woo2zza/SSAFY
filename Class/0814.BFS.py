
from collections import deque
#
# name=list(input().split()) # M B I K T S
# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]]
#
#
#
# def bfs(now):
#     q=deque()
#     q.append(now)
#     while q:
#         now=q.popleft()
#         print(name[now],end=' ')
#
#         for i in range(6):
#             if arr[now][i]==1:
#                 q.append(i)
#
# bfs(0)   # 0-> 탐색 시작 index


# Flood Fill
# n = int(input())
# arr = [[0]*n for _ in range(n)]
# y,x=map(int,input().split())
#
# arr[y][x] = 1
# q = deque()
# q.append([y,x])
#
# while q:
#     now = q.popleft()
#     y, x = now
#     directy = [0 ,0 ,1 ,-1]
#     directx = [1, -1 ,0 ,0]
#
#     for i in range(4):
#         dy = directy[i] + y
#         dx = directx[i] + x
#
#         if dy < 0 or dx < 0 or dy >= n or dx >= n: continue
#         if arr[dy][dx] != 0: continue
#
#         arr[dy][dx] = arr[y][x] + 1
#         q.append([dy,dx])
#
#     for i in arr:
#         print(*i)





# N입력받은 후 N*N 사이즈의 맵에 바이러스를 투입해 보자고 합니다. 0,1 좌표에는 며칠 날 바이러스가 도착할까?




n=int(input())
arr=[[0]*n for _ in range(n)]
y,x=map(int,input().split())

arr[y][x]=1
q=deque()
q.append((y,x,1))

ans=0
while q:
    y,x,level=q.popleft()
    # if y==0 and x==1:
    #     ans=level
    directy=[-1,1,0,0]
    directx=[0,0,-1,1]

    for i in range(4):
        dy=directy[i]+y
        dx=directx[i]+x

        if dy<0 or dx<0 or dy>=n or dx>=n: continue
        if arr[dy][dx]!=0: continue

        arr[dy][dx]=arr[y][x]+1
        q.append((dy,dx,level+1))
        if dy==0 and dx==1:
            ans=level+1
            break

for i in arr:
    print(*i)

print(ans)








