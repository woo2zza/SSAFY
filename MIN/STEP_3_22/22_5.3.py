n = int(input())
arr = ['x','o']
path = ['']* n
def abc(level):
    if level == n:
        for i in range(len(path)):
            print(path[i], end = '')
        print()
        return
    
    for i in range(2):
        path[level] = arr[i]
        abc(level + 1)
abc(0)