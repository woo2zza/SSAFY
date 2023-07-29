arr = [[0]*3 for i in range(3)]

num = int(input())
a = 2
for x in range(3):
    for y in range(a,3):
        arr[x][y] = num
        num += 1
    a -= 1
for j in arr:
    print(*j, sep = '')