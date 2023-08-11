arr = ['E','W','A','B','C']
st = input()
n = 4
path = [''] * n
used =[0] * len(arr)
def abc(level):

    if level == n:
        if st not in path:
            for i in range(n):
                print(path[i], end='')
            print()
        return

    for i in range(5):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = arr[i]
        abc(level + 1)
        used[i] = 0
abc(0)