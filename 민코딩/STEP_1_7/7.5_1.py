num = int(input())
arr = []
arr2 = []
for i in range(3):
    a=[]
    for j in range(5):
        a.append(num)
    arr.append(a)

for a in arr :
    print(*a, sep='')

for k in range(3):
    b = []
    for q in range(3):
        b.append(num)
    arr2.append(b)

for e in arr2:
    print(*e,sep = '')