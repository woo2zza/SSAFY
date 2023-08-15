arr = [1 ,2 ,3, 4, 5, 6]
lst = [
    [0 ,0, 1 ,0 ,1 ,1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1 ,0],
    [1 ,0 ,0 ,0 ,0, 0],
    [1 ,0 ,0 ,0 ,0, 0],
    [0 ,0 ,0 ,0 ,0, 0],
]
used = [0] * 6
count = 0
a, b = map(int, input().split())

def dfs(now):
     global count
     if now == b:
          count += 1
     for i in range(6):
          if lst[now][i]==1 and used[i]==0:
                used[i]=1
                dfs(i)
                used[i] = 1

used[a] = 1
dfs(a)
print(count)