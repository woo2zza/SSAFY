arr = [
    [4 ,5 ,4 ,5 ,4],
    [8 ,9 ,8 ,9 ,8],
    [1 ,2 ,1 ,2 ,1],
    [4 ,5 ,4 ,5 ,4],
    [6 ,7 ,6 ,7 ,6]
]
for i in range(5):
    number = list(map(int, input().split()))
    arr[number[0]][number[1]]+=1
    for x in range(5):
        for y in range(5):
            if arr[x][y] == 10:
                arr[x][y] = 0


for i in arr:
    print(*i, sep = '')