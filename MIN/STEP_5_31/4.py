arr = [list(input()) for _ in range(5)]
for i in range(5):
    temp = arr[i][3]
    arr[i][3] = arr[i][1]
    arr[i][1] = temp

Flag = 1
for i in arr:
    if ''.join(i) == 'MAPOM':
        Flag = 1
    else:
        Flag = 0
if Flag: print('yes')
else:
    print('no')