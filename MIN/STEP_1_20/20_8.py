num = int(input())
def abc(level):
    if level == 0:
        return
    abc(level // 2)
    print(level, end = ' ')
abc(num)