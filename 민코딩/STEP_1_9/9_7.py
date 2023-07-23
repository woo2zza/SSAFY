arr = [[] ,[] ,[] ,[] ,[] ,[]]
count = 0
for i in range(6):
    c, d = map(int, input().split())
    a = [0,0]
    a[0] = c
    a[1] = d
    arr[i] = a


for i in arr:
    if i[0] < i[1]:
        i[0], i[1] = i[1] , i[0]
        count += 1
for i in arr:
    print(*i)
print(count,'명', sep = '')