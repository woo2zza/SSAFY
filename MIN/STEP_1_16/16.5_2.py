arr = [[0] * 3 for i in range(6)]
a = 65
for y in range(2,-1,-1):
    for x in range(5,-1,-1):
        arr[x][y] = chr(a)
        a += 1

a,b = map(int, input().split())
print(arr[a][b])