arr = [[3,5,1],
       [3,8,1],
       [1,1,5]]

arr2 = [list(map(int, input().split())) for _ in range(2)]
Sum = 0
for i in range(2):
    for j in range(2):
        if arr2[i][j] == 1:
            # Sum += arr[i][j]
            print(i, j)