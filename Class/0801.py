'''
4 2 3 5
5 7 6 1
4 1 2 3

하드코딩 후 정수하나 입력받으면

1. 입력받은 정수가 존재하는지 존재여부 출력
'''

# arr = [list(map(int, input().split())) for _ in range(3)]
# target = int(input())
# flag = 0
# for i in range(3):
#     for j in range(4):
#         if arr[i][j] == target:
#             flag = 1
#             break
#         if flag == 1:
#             break
# if flag == 1: print('존재')
# else: print('없음')

# 2. '6'의 위치 찾기
# for i in range(3):
#     for j in range(4):
#         if arr[i][j] == 6:
#             print(f'({i},{j})')

# 3. 몇 번째 행의 합이 가장 클까요?
# Sum = 0
# max_sum = 0
# Maxind = 0
# for i in range(3):
#     Sum = 0
#     for j in range(4):
#         Sum += arr[i][j]
#         if max_sum < Sum:
#             max_sum = Sum
#             Maxind  = i + 1
# print(max_sum , Maxind)

# 4. 몇 번째 열의 합이 가장 작을까요?

# Min=21e8
# index=0
# sum=0
# for j in range(4):
#     sum=0
#     for i in range(3):
#         sum+=arr[i][j]
#     if sum<Min:
#         Min=sum
#         index=j
# print(index+1,Min)

# 5. 리스트에 숫자 6개 입력받고 누적합 구하고 누적합을 거꾸로 출력
# lst = list(map(int, input().split()))
# Sum = 0
# for i in range(1, len(lst)):
#     lst[i] += lst[i-1]
# print(lst[::-1])

# 6. 문자열을 하나와 정수 하나를 받고 입력받은 정수만큼 문자열을 우측으로 회전
# st = list(input())
# num = int(input())
#
# for i in range(num % len(st)):
#     temp = st[-1]
#     for j in range(len(st) ,0, -1):
#         st[i+1] = st[i]
#     st[0] = temp
# print(st)

# 7. target의 값이 lst 배열안에 존재하는지 출력

lst=[[4,2,3,5],
     [1,1,2,3],
     [4,7,6,4]]

target=[[8,4],
        [2,9]]
#
#
def isExist(value):
    for i in range(3):
        for j in range(4):
            if lst[i][j]==value:
                return 1
    return 0

for i in range(2):
    for j in range(2):
        ret=isExist(target[i][j])
        if ret: print('Y',end='')
        else: print('N',end='')
    print()

# 8. target배열의 값이 lst 배열에 각각 몇개 있는지 출력하기
# def isExist(num):
#     count = 0
#     for i in range(3):
#         for j in range(3):
#             if num == lst[i][j]:
#                 count += 1
#     return f'{num}:{count}'
#
#
#
# for i in range(2):
#     for j in range(2):
#         ret = isExist(target[i][j])
#         print(ret)

