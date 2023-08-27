# N, M = map(int, input().split())
# num = list(map(int, input().split()))
# path = [''] * 3
# used = [0] * len(num)
# lst = []
# def abc(card):
#     if card == 3:
#         if sum(path) <= M:
#             lst.append(sum(path))
#         return
#     for i in range(len(num)):
#         if used[i] == 1: continue
#         path[card] = num[i]
#         used[i] = 1
#         abc(card +1)
#         used[i] = 0
# abc(0)
# print(max(lst))

N, M = map(int, input().split())
num = list(map(int, input().split()))
Max = 0
ret= 0
# for i in range(0, N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             ret= num[i] + num[j] + num[k]
#             if Max < ret <= M:
#                 Max = ret
# print(Max)
