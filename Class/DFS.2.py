# 동전교환 / 거슬러 줄 돈을 입력받으면, 최소한의 동전 개수를 사용해서 거슬러주기
# N = int(input())
# coin = [110, 70, 10]
# Min = 2e46
# def dfs(level, money):
#     global Min
#     if money < 0:
#         return
#
#     if money == 0:
#         if level < Min:
#             Min = level
#
#     if level == 10:
#         return
#     for i in range(len(coin)):
#         dfs(level+1, money - coin[i])
#
# dfs(0, N)
# print(Min)

#T K B S  네명의 친구가 놀이동산에 갔습니다.
#놀이기구 1유닛의 자리는 3자리 입니다.
#4명 중 1명이 고소공포증이 있어서 놀이기구를 탈 수 없는 상황이라고 할때
#놀이기구를 탈 조합을 모두 출력해 주세요
# lv 3 br 4
# name="TKBS"
# path=['']*3
# def abc(level,start):
#     if level==3:
#         for i in range(3):
#             print(path[i],end=' ')
#         print()
#         return
#
#     for i in range(start,4):
#         path[level]=name[i]
#         abc(level+1,i+1)
#         path[level]=0
#
# abc(0,0)


# 두 라인에서 숫자를 하나씩 번갈아 가면서 선택
# 1번 라인에서 숫자1개.. 2번라인에서 숫자 1개..
# 첫번째 뽑은 숫자에 *1 을 할 것이며
# 두번째로 뽀는 숫자에는 *2 를 합니다.
# 세번쨰로 뽑은 숫자에는 *3 씩 하는 등,,, 모든값에 1씩 증가되는 값으로
# 가중치를 곱한 후 값들을 모두 더했을때... 0에 가장 가까운 수를 구하고자 합니다.
# 이때 총 합은 몇일까요??
# 각 라인에서 숫자는 1번씩만 사용하여 숫자를 뽑습니다.

# line1=[5,2,7,-5,-7,9]
# line2=[4,-5,-7,9,-5,3]
# used1=[0]*6
# used2=[0]*6
# ans=21e8
# Min=21e8
# def dfs(level,sum):
#     global Min,ans
#     if level==12:
#         if Min>abs(sum):
#             Min=abs(sum)
#             ans=sum
#         return
#
#     if level%2==0:
#         for i in range(6):
#             if used1[i]==1: continue
#             used1[i]=1
#             dfs(level+1,sum+(line1[i]*(level+1)))
#             used1[i]=0
#     else:
#         for i in range(6):
#             if used2[i]==1: continue
#             used2[i]=1
#             dfs(level+1,sum+(line2[i]*(level+1)))
#             used2[i]=0
#
# dfs(0,0)  # level # sum
# print(ans)



#플레이어 // 전투력
#a // 50
#b // 40
#c // 99
#d // 5
#e // 25
#f // 6
#g // 37

# 서바이벌 게임을 합니다. 선수와 각 선수의 전투력이 제공됩니다.
# a~g를 두 팀으로 나누어서 게임을 하고자 할때
# 두 팀의 최소 전투력 차이는 몇일까요?
# 모든 선수는 서바이벌에 참가 하며, 1인 팀도 가능 합니다.

# score=[50,40,99,5,25,6,37]
# Min=21e8
#
# def dfs(start,level,sum):
#     global Min
#
#     against=total-sum # B팀의 전투력
#     gap=abs(sum-against) # A팀과 B팀의 차이
#     Min=min(Min,gap) # 차이의 최소값 구하기
#
#     if level==6:
#         return
#     for i in range(start,7):
#         dfs(i+1,level+1,sum+score[i])
#
# total=sum(score)
# dfs(0,0,0)   #start #level #sum(팀A의 전투력)
# print(Min)
#
# arr = [
#     [0 ,0 ,0 ,0 ,1],
#     [1, 0, 1, 0 ,1],
#     [1 ,0, 1 ,0 ,1],
#     [1, 0 ,1 ,0, 0],
#     [0 ,0 ,0 ,0 ,0]
# ]
# y, x = map(int, input().split())
# used = [[0] * 5 for _ in range(5)]
# directy = [0, 0, -1 ,1]
# directx = [-1 ,1, 0, 0]
# Min = 32e43

#땅을 3번 개발하고자 한다 땅의  Max값 출력
import copy
arr=[[1,2,3],[4,5,6],[7,8,9]]
Max=-21e8

def digging(y,x):
    directy=[0,-1,1,0,0]
    directx=[0,0,0,-1,1]
    for i in range(5):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx]=(arr[dy][dx]*7)%10

def getsum():
    global arr
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=arr[i][j]
    return sum

def dfs(level):
    global Max, arr
    backup=copy.deepcopy(arr)
    if level==3:
        # arr배열 합을 확인한 후 최대값 갱신
        result=getsum()
        Max=max(result,Max)
        return

    for i in range(3):
        for j in range(3):
            digging(i,j)    #0,0~2,2
            dfs(level+1)
            arr=copy.deepcopy(backup)  # arr 배열 원상복구!!! 중요!!

dfs(0)   # level
print(Max)

