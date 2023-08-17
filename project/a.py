arr = [
    [],
    [3,5,6],
    [1,4],
    [5],
    [1],
    [1],
    []
]
A, B = map(int, input().split())
count = 0
Min = 2e14
used = [0] * 7
def dfs(now):
    global count, Min
    if now == B:
        if count > Min:
            Min = count
        return
    for i in arr[now]:
        if used[i] == 1:continue
        used[i] = 1
        count += 1
        dfs(i)
        count -= 1
        used[i] = 0

used[A] = 1
dfs(A)
print(Min)