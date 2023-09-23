N = int(input())
lst = list(map(int, input().split()))
lst.sort()
if lst[0] == 1:
    lst.remove(lst[0])

result = 0
for i in lst:
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        result += 1
print(result)