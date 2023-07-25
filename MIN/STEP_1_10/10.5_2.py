arr = [[0]*5 for i in range(5)]
a = 1
for x in range(4,-1,-1):
    for y in range(5):
        arr[y][x] = a
        a += 1

num = int(input())
for i in range(5):
    arr[num][i] = num
    


for j in arr:
    print(*j)