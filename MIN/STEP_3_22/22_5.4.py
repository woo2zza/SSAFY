a, b = map(int, input(). split())
arr = [[0]*3 for _ in range(2)]

for i in range(3):
    for k in range(3):
        arr[0][k] = a
        arr[1][k] = b

    for q in arr:
        print(*q)
    print()