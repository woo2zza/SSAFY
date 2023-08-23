T = int(input())
for q in range(1, T+1):
    N = int(input())
    lst = [[0] * 10 for _ in range(10)]
    arr = []
    for k in range(N):
        color = list(map(int, input().split()))
        for i in range(color[0], color[2]+1):
            for j in range(color[1], color[3]+1):
                lst[i][j] += color[4]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                cnt += 1
    print(f'#{q} {cnt}')