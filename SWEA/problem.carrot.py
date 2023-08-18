T = int(input())
for q in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    cnt = 1
    Max = 1
    for i in range(len(carrot)-1):
        if carrot[i] < carrot[i+1]:
            cnt += 1
            if Max < cnt:
                Max = cnt
        else: cnt = 1
    print(f'#{q} {Max}')




