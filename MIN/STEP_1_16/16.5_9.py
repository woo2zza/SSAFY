st = list(input().split())
arr = [[0]*int(st[1]) for i in range(int(st[0]))]
for k in range(2):
    for i in range(int(st[0])):
        for j in range(int(st[1])):
            arr[i][j] = st[2]
    for i in arr:
        print(*i, sep = '')
    print()

