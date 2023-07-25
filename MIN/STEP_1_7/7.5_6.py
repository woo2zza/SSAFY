arr = [[0,0,0,0],[0,0,0,0]]
y, x = map(int, input().split())
arr[y][x] = 1
for i in arr:
    print(*i)