import sys
sys.stdin = open("input.txt","r")

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [''] * M
used = [0] * len(lst)
ret = []
def abc(level):
    if level == M:
        ret.append(path[:])
        return
    for i in range(len(lst)):
        if used[i] == 1: continue
        path[level] = lst[i]
        used[i] = 1
        abc(level + 1)
        used[i] = 0

abc(0)
result = [list(item) for item in set(tuple(new) for new in ret)]

for i in result:
    print(*i)