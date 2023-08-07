T = int(input())
for q in range(1,T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    Max = -5e500
    Min = 5e100
    for i in range(N - M + 1):
        Sum = 0
        for j in range(i, i+M):
            Sum += num[j]
        if Sum > Max:
            Max = Sum
        if Sum < Min:
            Min = Sum
    print(f'#{q} {Max - Min}')