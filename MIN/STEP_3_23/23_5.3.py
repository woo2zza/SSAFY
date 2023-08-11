arr = [[' ']*4 for _ in range(4)]
arr2 = [list(map(int, input().split())) for i in range(3)]
for i in range(3):
    for j in range(3):
        arr[i][j] = arr2[i][j]

Sum = 0
total = 0
C = 0
for i in range(3):
    Sum = 0
    for j in range(3):
        Sum += arr[i][j]
    arr[i][3] = Sum

for i in range(3):
    total = 0
    for j in range(3):
        total += arr[j][i]
    arr[3][i] = total

for i in range(3):
    C += arr[i][i]
arr[3][3] = C

for i in arr:
    print(*i)