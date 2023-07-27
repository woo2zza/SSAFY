arr = [[0]*3 for i in range(2)]

num = list(map(int, input().split()))
for k in range(6):
    for i in range(2):
        for j in range(3):
            arr[i][j] = num[k]
            if num[k] == 0:
                num[k] = '#'

print(arr)
