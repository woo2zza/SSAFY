arr = ['A','B','C','D']
st = input()
path =['']*3
count = 1
def abc(level):
    global count
    if level == 3:
        # for i in range(len(path)):
        # if  path== st:
        print(count)
        return

    for i in range(4):
        path[level] = arr[i]
        abc(level + 1)
        count += 1
abc(0)