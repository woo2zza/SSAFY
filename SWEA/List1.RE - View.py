T = 10
for q in range(1, 10+1):
    N = int(input())
    lst = list(map(int, input().split()))
    Sum = 0
    for i in range(2, N-2):
            std_2 = lst[i] - lst[i - 2]
            std_1 = lst[i] - lst[i - 1]
            std1 = lst[i] - lst[i + 1]
            std2 = lst[i] - lst[i + 2]
            if std_2 > 0 and std_1 > 0 and std1 > 0 and std2 > 0:
                Sum += min(std_2, std_1, std1, std2)
    print(f'#{q} {Sum}')



