arr = [list(map(int, input().split())) for _ in range(3)]
arr2 = [
    [3 ,1 ,9],
    [7 ,2, 1],
    [1, 0 ,8]
]
Flag = False
for i in range(3):
    for j in range(3):
        if arr[i][j] == 1 and arr2[i][j] == 3 or arr2[i][j] == 4 or arr2[i][j] == 5:
            Flag = True

if Flag: print('발견')
else: print('미발견')
