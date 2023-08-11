arr = [[' ']*4 for _ in range(3)]
for i in range(3):
    a, b = map(int, input().split())
    arr[a][b] = '#'
