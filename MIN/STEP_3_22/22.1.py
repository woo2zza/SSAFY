path = [''] *2
alpa = ['A','B','C']
def abc(level):
    if level == 2:
        for i in range(2):
            print(path[i], end = '')
        print()
        return

    for i in range(3):
        path[level] = alpa[i]
        abc(level + 1)
abc(0)
