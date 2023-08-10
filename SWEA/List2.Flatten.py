T = 10
for q in range(1, T+1):
    check = int(input())
    dump = list(map(int, input().split()))

    for i in range(check):
        max_idx = dump.index(max(dump))
        dump[max_idx] -=1
        min_idx = dump.index(min(dump))
        dump[min_idx] +=1
    print(f'#{q} {dump[dump.index(max(dump))]-dump[dump.index(min(dump))]}')


