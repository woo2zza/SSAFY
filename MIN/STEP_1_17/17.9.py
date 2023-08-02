arr = [
    [3 ,7 ,4],
    [2 ,2 ,4],
    [2, 2 ,5]
]
target = list(map(int, input().split()))
bucket = [0] * 10
Max = bucket[0]
in_max = 0
for j in arr:
    for i in range(len(target)):
        if target[i] in j:
            bucket[target[i]] += 1

for i in range(len(bucket)):
    if bucket[i] > Max:
        Max = bucket[i]
        in_max = i
print(in_max)