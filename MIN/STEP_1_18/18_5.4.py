arr = [list(map(int, input().split()))  for _ in range(2)]
bucket = [0] * 5
for i in range(5):
    if arr[0][i] == 1:
        bucket[i] += 1
    if arr[1][i] == 1:
        bucket[i] += 1
Max = 0
for i in range(len(bucket)):
    if bucket[i] >=2 :
        Max +=1
print(f'{Max}개')
    