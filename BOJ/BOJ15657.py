N, M = map(int, input().split())
br = list(map(int, input().split()))
path = [''] * M
used = [0] * len(br)
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return

    for i in range(len(br)):
        path[level] = br[i]
        abc(level + 1)
abc(0)