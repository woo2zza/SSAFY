N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [i for i in range(N)]

path=[]
def dfs(now):
    path.append(now)
    for i in range(N):
        if arr[now][i] == 1:
            dfs(i)
dfs(0)



def abc(level):
    if level == 0:
        return
    # for i in range()
abc(0)