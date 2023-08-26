T = int(input())
for q in range(1, T+1):
    bucket = [0] * 1001
    N = int(input())
    for i in range(N):
        bus, st, ed = map(int, input().split())
        if bus == 1:
            for i in range(st, ed+1):
                bucket[i] += 1
        elif bus == 2:
            bucket[st] += 1
            bucket[ed] += 1
            if st % 2 == 0:
                for i in range(st+1, ed):
                    if i % 2 == 0:
                        bucket[i] += 1
            else:
                for i in range(st+1, ed):
                    if i % 2 == 1:
                        bucket[i] += 1

        elif bus == 3:
            bucket[st] += 1
            bucket[ed] += 1
            if st % 2 == 0:
                for i in range(st+1, ed):
                    if i % 4 == 0:
                        bucket[i] += 1
            else:
                for i in range(st+1, ed):
                    if i % 3 == 0 and i % 10 != 0:
                        bucket[i] += 1

    print(f'#{q}', end = ' ')
    print(max(bucket))