# 인접 행렬 / 인접 리스트
# 인접 행렬

# name = ['Amy','Bob','Chloe','Diane','Edger']
# arr = [
#     [0 ,1, 0 ,1, 0],
#     [0 ,0, 0 ,1, 0],
#     [0 ,1, 0 ,1, 0],
#     [0 ,0, 0 ,0, 1],
#     [1 ,0, 0 ,0, 0],
# ]
#
# Max = -1
# total = 0
# Maxindex = 0
# for i in range(5):
#     sum = 0
#     for j in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#     if sum > Max:
#         Max = sum
#         Maxindex = j
# print(name[Maxindex])

print('---------------------------------------------')
# 문자1개를 입력받고 입력받은 문자의 형제노드 출력
# 형제가 없다면 '형제없음' 출력

name = ['A','B','C','D','E','F']
arr=[[0,1,1,0,0,0],
     [0,0,0,1,1,0],
     [0,0,0,0,0,1],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

ch=input()
idx=ord(ch)-65

parents=-1
bro=-1

# 부모노드가 없다면 -> 형제없음

for i in range(6):
     if arr[i][idx]==1:
          parents=i
          break
if parents==-1:
     print('형제없음')
else:
     # 부모 인덱스를 탐색하며 형제 출력하기
     for i in range(6):
          if arr[parents][i]==1 and i!=idx:
               bro=i
               break
     if bro==-1:
          print('형제 없음')
     else:
          print(chr(i+ord('A')))

print('---------------------------------------------')

# name = ['A','B','C','D','E','F']
# arr=[[0,1,1,0,0,0],
#      [0,0,0,1,1,0],
#      [0,0,0,0,0,1],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]
#
# def dfs(now):
#     print(name[now], end = '')
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
# dfs(0)

print('---------------------------------------------')
#
# name = ['K','B','G','T','M','C']
#
# arr=[[0,0,0,0,0,0],
#      [1,0,1,1,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,1,1],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]
#
# def dfs(now):
#     print(name[now], end = '')
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
# dfs(1)

print('---------------------------------------------')
# name=['A','B','C','D']
# arr=[[0,1,1,0],
#      [0,0,1,1],
#      [1,1,0,1],
#      [0,0,0,0]]
# used=[0]*4
#
#
# def dfs(now):
#      print(name[now],end=' ')
#      for i in range(4):
#           if arr[now][i]==1and used[i]==0:
#                used[i]=1
#                dfs(i)
#
#
#
# used[0]=1 #탐색 시작하는 0번 인덱스에 해당하는 used 배열 값을 1체크하고
# dfs(0) # 0번 인덱스 부터 탐색 시작

print('---------------------------------------------------')

# name=['A','B','C','D']
# arr=[[0,1,1,0],
#      [0,0,1,1],
#      [1,1,0,1],
#      [0,0,0,0]]
# visited=[0]*4
#
# cnt=0
# def dfs(now):
#      global cnt
#      if name[now]=='D':
#           cnt+=1
#      for i in range(4):
#           if arr[now][i]==1 and visited[i]==0:
#                visited[i]=1
#                dfs(i)
#                visited[i]=0
#
# visited[0]=1
# dfs(0)
# print(cnt)

print('------------------------------------------------------')

# name=['A','B','C','D']
# arr=[[0,4,8,0],
#      [0,0,1,7],
#      [0,1,0,3],
#      [0,0,0,0]]
# used=[0]*4
# Min=21e8
#
# def dfs(now,sum):
#      global Min
#      if now==3:
#           if sum<Min:
#                Min=sum
#      for i in range(4):
#           if arr[now][i]>0 and used[i]==0:
#                used[i]=1
#                dfs(i,sum+arr[now][i])
#                used[i]=0
# used[0]=1
# dfs(0,0)    #탐색시작0  sum0
# print(Min)