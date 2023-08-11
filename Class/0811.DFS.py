# name='ABCDEF'
# n,m=map(int,input().split())
# lst=[[] for _ in range(n)]
# for i in range(m):
#      s,e=map(int,input().split())
#      lst[s].append(e)
#
# def dfs(now):
#      print(name[now],end=' ')
#      for i in lst[now]:
#           dfs(i)
# dfs(0)
#
# #

#각 층에서 숫자 1개씩 택하여 계단을 내려옵니다.
#4개의 층에서 택한 숫자들의 합이 20 이상인 경우는 몇가지 일까요??

# arr=[[4,5,2],
#      [-2,1,6],
#      [3,9,-4],
#      [3,5,2]]
# cnt = 0
# def dfs(level, sum):
#         global cnt
#         if level == 4:
#             if sum >= 20:
#                 cnt += 1
#
#             return
#         for i in range(3):
#             dfs(level + 1, sum + arr[level][i])
# dfs(0,0)
# print(cnt)

arr = [
    [3 ,5 ,9 ,6],
    [7, -8, 1, 6],
    [-10, 2, 3, 9],
    [5, 1, 2 ,8],
    [4, 7 ,1 ,8]
]
cnt = 0
def dfs(level, sum):
    global cnt
    if level == 5:
        if sum >=30:
            cnt+=1
        return
    for i in range(4):
        if arr[level][i-1] < 0 or arr[level][i-1] > 3 : continue
        dfs(level +1 , sum + arr[level][i] + arr[level][i-1] + arr[level][i+1])
dfs(0,0)
print(cnt)