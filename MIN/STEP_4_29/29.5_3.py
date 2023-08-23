arr = [list(map(int, input().split())) for _ in range(3)]
Flag = 1
idx = 0
for j in range(3):
    for i in range(2):
        if arr[j][i] == arr[j][i+1]:
            Flag = 1
            idx = arr[j][1]
        else: 
            Flag = 0
    if Flag : print(idx)
    else: print('x')
    