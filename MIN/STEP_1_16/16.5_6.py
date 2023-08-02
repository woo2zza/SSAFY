st = list(input())
maxindex = 0
minlndex = 0
Max = 'A'
Min = 'Z'
for i in range(len(st)):
    if Max < st[i]:
        Max = st[i]
        maxindex = i
    if Min > st[i]:
        Min = st[i]
        minlndex = i
print(maxindex)
print(minlndex)
