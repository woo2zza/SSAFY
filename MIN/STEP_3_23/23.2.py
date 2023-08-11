st = list(input())
path = [''] * 4
used = [0] *4
used = [0] * len(st)
count = 0
def abc(level):
    global count
    if level == 4:
        count += 1
        return
    for i in range(4):
        if level > 0 and path[level -1] == 'T' and st[i] == 'B':continue
        if level > 0 and path[level -1] == 'B' and st[i] == 'T':continue
        
        path[level] = st[i]
        abc(level + 1)
abc(0)
print(count)