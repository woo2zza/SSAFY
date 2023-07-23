a, b = input().split()
arr = [] *3
for i in range(4):
    arr.append(a)
for i in range(4,6):
    arr.append(b)


for i in range(3):
    print(*arr, sep = '')
