T = int(input())
for q in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-1):
            if num[j] > num[j +1]:
                num[j], num[j+1] = num[j +1] , num[j]
    
    print(f'#{q}', end = '')
    for i in num:
        print(i, end = ' ')
    print()