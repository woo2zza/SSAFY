T = int(input())
for k in range(1,T+1):
    N , M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst2 = [[0]*M for _ in range(M)]

    def find(x, y):
        Sum = 0
        for i in range(M):
            for j in range(M):
                Sum += lst[i+x][j+y]
        return Sum
    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if find(i, j) > Max:
                Max = find(i,j)
        
    print(f'#{k} {Max}')