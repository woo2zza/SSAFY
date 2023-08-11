st = list(input())
path = [''] * 4
used = [0] *4
def abc(level):
    if level == 4:
        return
    for i in range(4):
        path[level] = st[i]
        abc(level + 1)
abc(0)