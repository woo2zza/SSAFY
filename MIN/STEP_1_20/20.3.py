num1 = list(map(int, input().split()))
def num(level):
    print(num1[level-1], end = ' ')
    if level == len(num1):
        return
    num(level + 1)
    print(num1[level-1], end = ' ')

num(1)
