T = int(input())
for q in range(1, T +1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    number = []
    for i in num:
        cnt = 0
        while N % i == 0:
            cnt += 1
            N /= i
        number.append(cnt)
    print(f'#{q}', end = ' ')
    for i in number:
        print(i, end = ' ')
    print()
