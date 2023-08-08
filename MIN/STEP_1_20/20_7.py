arr = [3 ,7, 4 ,1 ,9 ,4, 6 ,2]
num = int(input())
def abc(level):
    print(arr[level], end = ' ')
    if level == 0:
        return

    abc(level - 1)
    print(arr[level], end = ' ')


abc(num)