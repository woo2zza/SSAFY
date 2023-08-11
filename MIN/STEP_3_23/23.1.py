name = list(input())
path = [' '] * 3
used = [0] * 4
def abc(level):
    if level == 3:
        for i in range(3):
            print(path[i], end = '')
        print()
        return

    for i in range(4):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = name[i]
        abc(level +1)
        used[i] = 0

abc(0)