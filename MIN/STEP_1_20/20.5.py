st = list(input())
def abc(level):

    print(st[level], end = '')
    if level == 4:
        print()
        print(st[level], end = '')
        return
    abc(level +1)
    print(st[level], end = '')
abc(0)
