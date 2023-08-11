a = []
for i in range(4):
    st = list(input())
    a.append(st)

a.sort(key = len)

for i in a:
    print(*i, sep = '')