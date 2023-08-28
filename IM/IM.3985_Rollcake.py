# import sys
# sys.stdin = open("input.txt","r")

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

print(lst)
