T = int(input())
for q in range(1, T + 1):
    N = int(input())
    num = input()
    A = num.split('0')
    Max = 0
    for i in A:
        if Max < len(i):
            Max = len(i)


    print(f'#{q} {Max}')