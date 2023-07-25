a, b, c = map(int, input().split())
arr = [[0]*4 for i in range(3)]

for i in range(4):
    arr[0][i] = a
    a += 1

for i in range(4):
    arr[1][i] = b
    b += 1

for i in range(4):
    arr[2][i] = c
    c += 1

for j in arr:
    print(*j)
