N = int(input())
lst = [i for i in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
path = [''] * N
def abc(now):
    
    for i in range(N):
        if arr[now][i] ==1:
            path[i] = lst[i]
            print(path[i], end = '')
            abc(i)
            
abc(0)