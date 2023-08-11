T = int(input())
for q in range(1,T+1):
    N = int(input())
    arr = list(map(int, input()))
    bucket = [0] * 10
    for i in range(len(arr)):
        bucket[arr[i]] += 1
    
            
    Max = 0
    idx = 0
    
    for i in range(len(bucket)):
        if bucket[i] >= Max:
            Max = bucket[i]
            idx = i
    
    
    print(f'#{q} {idx} {Max}')