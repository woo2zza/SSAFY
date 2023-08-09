num = int(input())
a = []
for i in range(num):
    a.append(i)
path = [''] * 4
def abc(level):
    if level == 2:
        for i in range(len(path)):
            print(path[i], end = '')
        print()
        return

    for i in range(2):
        path[level] = a[i]
        abc(level+1)

abc(0)