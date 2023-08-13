T = int(input())
for q in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direx = [-1, 1, 0,0,0]
    direy = [0,0,1,-1,0]
    arr2 = []
    def find(a, b):
        multi = 0
        for i in range(5):
            dx = a+direx[i]
            dy = b + direy[i]
            if dx > N-1 or dx < 0 or dy > M -1 or dy < 0: continue
            multi += arr[dx][dy]
        return multi
    Max = 0 
    for i in range(N):
        for j in range(M):
            ret = find(i, j)
            if Max < ret:
                Max = ret
    print(f'#{q} {Max}')