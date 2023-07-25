arr = []
A, B = map(int, input().split())
for j in range(3):
    a = [0,0,0]
    for i in range(3):
        a[i] = A
    arr.append(a)
for k in range(4,7):
    b = [0,0, 0]
    for q in range(3):
        b[q] = B
    arr.append(b)

for i in arr:
    print(*i, sep = '')