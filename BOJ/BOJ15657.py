N, M = map(int, input().split())
br = list(map(int, input().split()))
br.sort()
path = [''] * M
used = [0] * len(br)
lst = []
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return

    for i in range(len(br)):
        if level > 0 and path[level -1] > br[i] : continue
        path[level] = br[i]
        abc(level + 1)
abc(0)