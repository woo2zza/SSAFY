T = int(input())
for q in range(1, T + 1):
    N = int(input())
    bucket = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            bucket[j] += 1

    s = int(input())
    ret = [0] * s
    for k in range(s):
        C = int(input())
        ret[k] = bucket[C]

    print(f'#{q}', *ret)