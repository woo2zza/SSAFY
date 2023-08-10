num = [i+1 for i in range(int(input()))]
path = [''] * 4
def abc(level):
    if level == 4:
        for i in range(len(path)):
            print(path[i], end = '')
        print()
        return

    for i in range(len(num)):
        path[level] = num[i]
        abc(level+1)

abc(0)