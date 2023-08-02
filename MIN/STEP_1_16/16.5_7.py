arr = [[0]*4 for i in range(7)]
a=1
for x in range(7):
    for y in range(4):
        arr[x][y] = a
        a += 1

a,b,c = map(int, input().split())

for x in range(4):
    arr[a][x] = 0
    arr[b][x] = 0
    arr[c][x] = 0


for i in arr:
    print(*i)