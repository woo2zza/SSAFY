N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
print(lst)
ret = 0
for i in range(1, len(lst)+1):
    ret += (lst[i-1] * i)
print(ret)