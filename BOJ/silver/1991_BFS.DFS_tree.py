N = int(input())
arr = [[0] * 26 for _ in range(N+1)]
used = [[0] * 26 for _ in range(N+1)]
for i in range(N):
    a, b, c = input().split()
    if 65 <= ord(b) <= 90:
        arr[ord(a)-65][ord(b)-65] = 1
    if 65 <= ord(c) <= 90:
        arr[ord(a)-65][ord(c)-65] = 1


def dfs(i,j):
    print(chr(j+65), end = '')
    for k in range(26):
        if arr[j][k] == 1:
            if used[j][k] == 1: continue
            used[j][k] = 1
            dfs(j,k)

for i in range(N+1):
    for j in range(26):
        if arr[i][j] == 1:
            used[i][j] = 1
            dfs(i, j)












for i in arr:
    print(*i)

    