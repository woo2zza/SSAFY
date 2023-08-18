T = int(input())
for q in range(1, T+1):
    M , N = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]

    directy = [0,0,1,-1]
    directx = [1,-1,0,0]


    def pang(y , x):
        global Sum
        for j in range(1, lst[y][x]):
            for i in range(4):      
                dy = y + directy[i]*j
                dx = x + directx[i]*j
                if dy > M -1 or dy < 0 or dx > N -1 or dx < 0:
                    continue
                Sum += lst[dy][dx]
        return Sum

    Max = 0
    for i in range(M):
        for j in range(N):
            Sum = 0
            ret = pang(i, j)
            if Max < ret:
                Max = ret
    print(f'#{q} {Max}')