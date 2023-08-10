arr = ['A','B','C','D']
st = input()
path =['']*3
def abc(level):
    count = 0
    if level == 3:
        for i in range(len(path)):
            count += 1
            if path[i] == st:
                print(count)
        return

    for i in range(4):
        path[level] = arr[i]
        abc(level + 1)
abc(0)