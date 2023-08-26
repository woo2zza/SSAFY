T = int(input())
for w in range(1, T+1):
    bucket = [0] * (5001)

    test = int(input())
    for i in range(test):
        a, b = map(int, input().split())
        for q in range(a, b+1):
            bucket[q] += 1
    A = []
    P = int(input())
    for i in range(P):
        station = int(input())
        A.append(bucket[station])
    print(f'#{w}', end = ' ')
    for i in A:
        print(i, end = ' ')
    print()
