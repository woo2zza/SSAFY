a, b = map(int, input().split())
arr = [[10,16,22],[11 ,17 ,23],[12 ,18 ,24],[13 ,19 ,25],[14 ,20 ,26],[15 ,21 ,27]]

for i in range(a, b+1):
    for j in range(3):
        arr[i][j] = 7

for k in arr:
    print(*k)