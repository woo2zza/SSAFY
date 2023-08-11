num = int(input())
arr = ['B','T','S','K','R']
path = [''] * num
count = 0
used = [0] * len(arr)
def abc(level):
    global count
    if level == num:
        if 'S' in ''.join(path):
            count += 1
        return
    for i in range(5):
        if used[i] == 1:continue
        used[i] = 1
        path[level] = arr[i]
        abc(level + 1)
        used[i] = 0
abc(0)
print(count)

