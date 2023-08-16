N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
path = [0] * 3

def abc(level, now):
    if level == 2:
        for i in range(3):
            print(path[i] , end = ' ')
        print()
        return

    for i in range(N):
        if arr[now][i] == 1:
            path[level+1] = i
            abc(level + 1, i)

abc(0,0 )