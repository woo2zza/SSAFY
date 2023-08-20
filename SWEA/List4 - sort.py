T = int(input())
for q in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    lst = []
    Max = 0
    Min = 3e98
    while number:
        lst.append(max(number))
        number.remove(max(number))
        lst.append(min(number))
        number.remove(min(number))
        if len(lst) == 10: break
    print(f'#{q}', end = ' ')
    print(*lst)