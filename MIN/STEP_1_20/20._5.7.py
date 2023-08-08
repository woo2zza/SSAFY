st = list(input())
for i in range(1,len(st)+1):
    for j in range(i):
        print(st[j], end='')
    print()