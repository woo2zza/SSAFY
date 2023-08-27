# import sys
# sys.stdin = open("input.txt","r")

# lst = []
# for _ in range(9):
#     height = int(input())
#     lst.append(height)

# Sum = 0
# for i in range(len(lst)):
#     Sum += lst[i]

# multi = 0
# real_short = []
# for i in range(len(lst)-1):
#     flag = 1
#     for j in range(i+1, len(lst)):
#         multi = lst[i] + lst[j]
#         if Sum - multi == 100:
#             lst[i] = 0
#             lst[j] = 0
#             flag = 0
#             break
#     if flag == 0 :
#         break


# lst.sort()
# for i in lst:
#     if i != 0:
#         print(i)

# def solve():
#     N = 9
#     num = sum(lst) - 100
#     for i in range(N-1):
#         for j in range(i +1, N):
#             if lst[i] + lst[j] ==num:
#                 return lst[i] , lst[j]


# lst = [int(input()) for _ in range(9)]
# n, m = solve()  # 7명의 포함되지 않는 두명 찾기
# for i in sorted(lst):
#     if i != n and i != m:
#         print(i)


lst = []
for i in range(9):
    hight = int(input())
    lst.append(hight)
lst.sort()
for i in range(0, len(lst)-1):
    for j in range(i+1, len(lst)):
       if sum(lst) - (lst[i] + lst[j]) == 100:
           result = lst[i]
           result2 = lst[j]
lst.remove(result)
lst.remove(result2)

for i in lst:
    print(i)