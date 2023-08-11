arr = ['A','B','C','D']
st = input()
path =['']*3
a = []
count =0
tmp = 0
def abc(level):
    global count, tmp
    if level == 3:
        count += 1
        if ''.join(path) == st:
            tmp = count
        return

    for i in range(4):
        path[level] = arr[i]
        abc(level + 1)

abc(0)
print(f'{tmp}번째')
