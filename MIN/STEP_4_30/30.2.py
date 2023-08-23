k = int(input())
arr = [
    [0, 0 ,1 ,0, 2 ,0],
    [5, 0 ,3, 0, 0 ,0],
    [0 ,0 ,0 ,0, 0, 7],
    [2 ,0, 0, 0, 8, 0],
    [0, 0, 9, 0, 0, 0],
    [4, 0, 0, 7, 0, 0]
]
Sum = 0
used = [0] * 6
def dfs(now, sum):
    global Sum 
    print(now, sum)
    for i in range(6):
        if used[i] == 1: continue
        
        if arr[now][i] > 0:
            used[i] = 1
            Sum += arr[now][i]
            dfs(i,Sum)

            

used[k] = 1
dfs(k,0)