arr = [[0]*4 for i in range(4)]
z = 0
for x in range(4):
    num = list(map(int, input().split()))
    for y in range(4):
        arr[x][y] = num[z]
        z += 1






for i in arr:
    print(*i)