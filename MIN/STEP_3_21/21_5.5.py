lst = list(map(int, input().split()))
bucket = [0] * 11
result = [0] * len(lst)
for i in range(len(lst)):
    bucket[lst[i]] += 1

for i in range(1, len(bucket)):
    bucket[i] = bucket[i] + bucket[i-1]

for i in range(len(lst)):
    bucket[lst[i]]-=1
    result[bucket[lst[i]]] = lst[i]
print(result)