arr = ['A','B','C']
num = int(input())
path = [' '] * num
cnt = 0
def abc(level):
    global cnt
    if level == num:
        cnt += 1
        return
    for i in range(3):
        if level > 1 and path[level-1] == arr[i] and path[level-2] == arr[i]: continue
        path[level] = arr[i]
        abc(level +1)
abc(0)
print(cnt)