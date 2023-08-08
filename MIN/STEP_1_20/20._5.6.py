st = list(map(int, input().split()))
for i in range(4,len(st)+1):
    for j in range(i):
        print(st[j], end = ' ')
    print()