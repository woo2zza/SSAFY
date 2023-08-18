T = int(input())
for q in range(1, T +1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    bucket = [0] * 10
    Flag = 1
    for i in range(9):
        for j in range(9):
            bucket[lst[i][j]]
    for i in bucket:
        if i > 0 and i != 9:
            Flag = 0
    if Flag == 1: 1
    else: 0
    print(f'#{q} {Flag}')
    