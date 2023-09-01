
T = int(input())
for q in range(1, T+1):
    st1 = list(input())
    st2 = list(input())
    bucket = [0] * 100
    for i in range(len(st1)):
        for j in range(len(st2)):
            if st1[i]==st2[j]:
                bucket[i] +=1
    print(f'#{q}', end = ' ')
    print(max(bucket))