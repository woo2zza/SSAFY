num = int(input())
lst = list(input().split())
path = [''] *2
used = [0] * num

cnt = 0


def abc(level, st):
    global cnt
    if level == 2:
        if ''.join(path) == 'HITSMUSIC':
            cnt += 1

        return

    for i in range(st, num):
        if used[i] == 1: continue
        path[level] = lst[i]
        used[i] = 1
        abc(level+1, i)
        used[i] = 0
abc(0, 0)
print(cnt)