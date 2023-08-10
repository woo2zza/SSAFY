a = int(input())
arr = [
    [[2,4],[1,5]],
    [[2,3],[3,6]],
    [[7,3],[1,5]]
]
for i in arr:
    for k in arr[i][a]:
        Max = max(k)
        Min = min(k)
print(Max)
print(Min)