arr = [[0,0,0],[0,0,0],[0,0,0]]
n1, n2, n3 = map(int, input().split())
for i in arr:
    for k in i:
        arr[n1][n2] = n3
    
for i in arr:
    print(*i)