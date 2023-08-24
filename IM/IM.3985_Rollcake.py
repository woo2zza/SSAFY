import sys
sys.stdin = open("input.txt","r")

# cake = int(input())
# people = int(input())
# bucket = [0] * (cake+1)
# bucket2 = [0] * (cake+1)
# mius_arr = [0]
# Max = 0
# for i in range(1, people+1):
#     st, ed = map(int, input().split())
#     mius = ed - st
#     mius_arr.append(mius)
#     for q in range(st, ed+1):
#         if bucket[q] != 0: continue
#         bucket[q] = i
# for i in bucket:
#     bucket2[i] +=1
#
# Buck = Mius = min_idx = Buck_idx = 0
# for i in range(1, len(mius_arr)):
#     if mius_arr[i] > Mius:
#         Mius = mius_arr[i]
#         min_idx = i
#
# for i in range(1, len(bucket2)):
#     if bucket2[i] > Buck:
#         Buck = bucket2[i]
#         Buck_idx = i
#
#
# print(min_idx)
# print(Buck_idx)

L = int(input())
N = int(input())
lst = [1] * (L+1)
msx1 = mx2 = mx1_i = mx2_i = 0
for i in range(1, N +1):
    s, e = map(int, input().split())
    if msx1 < (e-s):
        msx1, mx1_i = e-s , i

    cnt = sum(lst[s:e+1])
    if mx2 < cnt:
        mx2, mx2_i = cnt, i
    lst[s:e+1] = [0] * (e-s+1)
print(mx1_i)
print(mx2_i)