st = list(input())
for i in range(len(st), 0,-1):
    for j in range(i-1,len(st)):
        print(st[j], end = '')
    print()
