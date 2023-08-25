import sys
sys.stdin = open("input.txt","r")

Y, X = map(int, input().split())
arr = [list(input()) for _ in range(Y)]

re = [[-1] * X for _ in range(Y)]
for i in range(Y):
    cnt = -1
    for j in range(X):
        if arr[i][j] == 'c':
            cnt = 0
        else:
            if cnt >= 0:
                cnt += 1
        re[i][j] = cnt


for i in re:
    print(*i)