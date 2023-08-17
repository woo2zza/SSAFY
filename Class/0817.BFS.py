from collections import deque
#
# arr = [[0] *4 for _ in range(4)]
# y1, x1 = map(int, input().split())
# arr[2][1] = 1
# q = deque()
# q.append((2,1,1))
# ans = 0
# directy = [0 ,0, 1, -1]
# directx = [1, -1, 0, 0]
#
# while q:
#     y,x,level = q.popleft()
#
#     for i in range(4):
#         dy = y + directy[i]
#         dx = x + directx[i]
#
#         if dy < 0 or dy > 3 or dx < 0 or dx > 3:continue
#         if arr[dy][dx] != 0: continue
#         arr[dy][dx] = arr[y][x] + 1
#         q.append((dy,dx,level +1))
#
#         if dy == y1 and dx == x1:
#             ans = arr[dy][dx]
# for i in arr:
#     print(*i)
# print(ans)
#
# arr = [1,2,3,4,5,6]
# lst = [
#     [],
#     [2],
#     [4,5],
#     [2,4,5],
#     [1,2],
#     [6],
#     []
# ]
#
# q = deque()
# q.append(2)
# used = [0] *7
# used[2] = 1
#-----------------------------------------------------
# arr=[[0,0,0,0,0,0],
#      [1,0,0,0,1,0],
#      [1,0,0,0,1,0],
#      [0,0,0,0,0,0]]
# directy=[0,0,-1,1]
# directx=[1,-1,0,0]
#
# answer=0
#
# def bfs(sty,stx,edy,edx):
#     q=deque()
#     q.append([sty,stx,0])
#     used=[[0]*5 for _ in range(4)]
#     used[sty][stx]=1
#     while q:
#         now=q.popleft()
#         yy,xx,level=now
#         if yy==edy and xx==edx:
#             return level
#
#         for i in range(4):
#             dy=directy[i]+yy
#             dx=directx[i]+xx
#
#             if dy<0 or dy>3 or dx<0 or dx>4: continue
#             if used[dy][dx]==1: continue # 중복
#             if arr[dy][dx]==1: continue # 벽X
#             used[dy][dx]=1   # 중복 체크 배열에 1 체크하기
#             q.append([dy,dx,level+1])
#
# answer+=bfs(0,0,3,0)
# answer+=bfs(3,0,3,4)
# print(answer)



#----------------------------------------------------------



















