import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [''] * M
used = [0] * N
ret = []
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return ret
    lab = 0
    for i in range(N):
        if used[i] == 1: continue
        if lab == lst[i]: continue
        path[level] = lst[i]
        lab = lst[i]
        used[i] = 1
        abc(level+1)
        used[i] = 0

abc(0)
