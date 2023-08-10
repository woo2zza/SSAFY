T = int(input())
for q in range(1,T+1):
    N = int(input())
    num = list(input())
    print(num)
    bucket = [0] * 10
    for i in range(len(num)):
        bucket[int(num[i])] += 1
    
            
    Max = max(bucket[i])
    idx = 0
    
    for i in range(len(bucket)):
        if bucket[i] > Max:
            Max = bucket[i]
            idx = i
    
    
    print(f'#{q} {idx} {Max}')