lst = [4, 3 ,5 ,1 ,7 ,5 ,6 ,8 ,1, 6 ,9 ,5]
# target 이라는 리스트에 0~7 사이의 정수 3개 입력받기 n이라는 변수에 1~5 사이의 정수를 입력받기

# target = list(map(int, input().split()))
# n = int(input())
# Max = -21e8
# answer = 0
# def getsum(t):
#     sum = 0
#     for i in range(t,t+n):
#         sum += lst[i]
#     return sum
#
# for i in range(len(target)):
#     ret = getsum(target[i])
#     if ret>Max:
#         Max = ret
#         answer = target[i]
# print(answer, Max)

# 내답
# arr = []
# total = 0
# for j in range(len(target)):
#     for i in range(n):
#         total += lst[target[j] + i]
#     arr.append(total)
#     total = 0
#
# print(max(arr))

# 연속된 숫자 3개의 합이 가장 클 때 의 값을 출력해 주세요
# lst = [
#     [4 ,5 ,2 ,6 ,7 ,3 ,1],
#     [2, 9, 9, 6, 1, 6, 7]
# ]
# Max = -21e8
# def getsum(y,x):
#     total = 0
#     for i in range(3):
#         total += lst[y][x + i]
#     return total
#
# for i in range(len(lst)):
#     for j in range(5):
#         ret = getsum(i,j)
#         if ret > Max:
#             Max = ret
# print(Max)

#-------------------------------------------------------

# 1 2 3 4 5
# 2 4 2 1 3
# 3 4 5 2 5
#
# 3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!
#
# 정답은:
# 0 2
# 2 0
#
# arr = [
#     [1, 2, 3, 4, 5],
#     [2, 4, 2, 1, 3],
#     [3, 4, 5, 2, 5]
# ]
# p = [3, 4, 5]
# idx = 0
#
# def IsPatten(i,j):
#     for i in range(3):
#         if p != arr[i][j + i]:
#             return 0
#     return 1
#
#
# for x in range(3):
#     for y in range(3):
#         ret = IsPatten(x,y)
#         if ret:
#             print(i,j)

# --------------------------------------------------------
# lst = [
#     [1 ,2, 3, 4, 5],
#     [2 ,4 ,2 ,1 ,3],
#     [3 ,4 ,5 ,2 ,5]
# ]
#
# target = [[3, 4],
#           [2, 1]]   # 의 좌표는?
#
#
#
# def findpt(x,y):
#     for i in range(2):
#         for j in range(2):
#             if lst[x+i][y+j] != target[i][j]:
#                 return 0
#     return 1
#
#
# for i in range(2):
#     for j in range(4):
#         ret = findpt(i,j)
#         if ret:
#             print(i,j)

# ---------------------------------------------------------
arr = [[1, 5, 4 ,2],
       [1, 3, 4 ,2],
       [3 ,5 ,3 ,2],
       [2 ,6 ,4 ,1]]

# ***  이 모양으로 땅을 갖을 수 있을 때
# ***  배열의 합을 구하여라

# def findpt(i,j):
#     total = 0
#     arr2= []
#     for x in range(2):
#         for y in range(3):
#             total += arr[i+x][j+y]
#         arr2.append(total)
#     return max(arr2)
#
#
# for x in range(3):
#     for y in range(2):
#         ret = findpt(x,y)
# print(ret)
# n=int(input())
# a=list(map(int,input().split()))
#
# bucket=[0]*10
#
# for i in range(len(a)):
#     bucket[a[i]]+=1
#
# for i in range(len(bucket)):
#     if bucket[i]!=0:
#         print(f'{i} : {bucket[i]}개 있음')
#
# --------------------------------------------------------
# st = list(input())
# bucket = [0] * 26
# for i in range(len(st)):
#     index = ord(lst[i]) - ord('a')
#     bucket[index] += 1

# --------------------------------------------------------
# n개의 정수를 입력받은 후
# counting sort (O(n)의 속도로 오름차순 정렬)
# (1~10사이의 숫자를 입력받는다고 가정하자)
n = int(input())
a = list(map(int, input().split()))
bucket = [0] * 11
# 버켓 등록
for i in a:
    bucket[i] += 1

# 누적합 구하기
for i in range(1, len(bucket)):
    bucket[i] += bucket[i - 1]

# 값넣기
result = [0] * n
for i in range(n):
    bucket[a[i]] -= 1
    index = bucket[a[i]]
    result[index] = a[i]

# 출력하기
print(*result)
