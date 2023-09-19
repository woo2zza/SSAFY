import sys
sys.stdin = open("SSAFY/BOJ/Silver/input.txt","r")

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [''] * M
used = [0]*N


def abc(start , level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return
    new = 0
    for i in range(start, N):
        if used[i] == 1: continue
        if new == lst[i] : continue
        new = lst[i]
        path[level] = lst[i]
        used[i] = 1
        abc(i, level + 1)
        used[i] = 0

abc(0, 0)