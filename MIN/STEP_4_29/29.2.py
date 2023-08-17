arr = [
    [],
    [3,5,6],
    [1,4],
    [5],
    [1],
    [1],
    []
]
Flag = 1
visited= [0] * 7
count = 0
Min = 3e24
A , B = map(int, input().split())
def dfs(now):
    global count, Min
    
    if now == B:
        if Min > count:
            Min = count
    
        return 
    
    for i in arr[now]:
        if visited[i] == 1: continue
        count += 1
        visited[i] = 1
        dfs(i) 
        count -=1   
        visited[i] = 0

visited[A] = 1
dfs(A)
if Min == 3e24:
    print(0)
else:
    print(Min)