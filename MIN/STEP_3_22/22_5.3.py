st = input()
A = ord(st)
arr = [list([0] * 3 for _ in range(3)) for i in range(3) ]

for i in arr:
    for j in range(3):
        for k in range(3):
            arr[j][k] = chr(A)
    A += 1
    for q in arr:
        print(*q, sep = '')
    print()