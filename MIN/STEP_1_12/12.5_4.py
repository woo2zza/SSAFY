arr = [[0]*5 for i in range(5)]
num = int(input())

for x in range(5):
    for y in range(5):
        arr[0][y] = num
        arr[4][y] = num
        arr[x][0] = num
        arr[x][4] = num

for x in range(1,4):
    for y in range(1,4):
        arr[x][y] = '_'

for ar in arr:
    print(*ar, sep = '')