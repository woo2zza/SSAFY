T = int(input())
for q in range(1, T+1):
    bucket = [0] * 101
    num = int(input())
    lst = list(map(int, input().split()))
    for i in lst:
        bucket[i]+=1
    Max = 0
    for j in range(len(bucket)):
        if bucket[j] >= Max:
            Max = bucket[j]
            Max_idx = j
    print(f'#{q} ', end = '')
    print(Max_idx)