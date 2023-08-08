arr = [list(map(int, input().strip().split())) for _ in range(4)]
input()
arr2 = [list(map(int, input().strip().split())) for _ in range(4)]
for i in range(4):
    for j in range(4):
        if arr[i][j] == arr2[i][j] and arr2[i][j]==1:
            print('걸리다')
        else:
            print('걸리지않는다')