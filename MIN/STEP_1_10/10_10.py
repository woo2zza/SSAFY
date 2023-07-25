
arr = [[0]*4 for i in range(3)]
a = 12
for x in range(3):
    for y in range(4):
        arr[x][y] = a
        a -= 1
num = int(input())

for i in range(3):
    arr[i][num] = 0

for k in arr:
    print(*k)