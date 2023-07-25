arr = [[0]*4 for i in range(4)]
a = 2
b = 0
for x in range(4):
    for y in range(4):
        arr[y][x] = a
        a += 2
for k in arr:
    print(*k)
