arr = [
    [3, 4 ,1 ,6],
    [3 ,5 ,3 ,6],
    [0, 0, 0, 0],
    [5 ,4 ,6 ,0]
]

num = list(map(int, input().split()))
for i in range(4):
    arr[2][i] = num[i]
max = min = arr[0][0]
max_y = max_x = min_y = min_x = 0
for y in range(4):
    for x in range(4):
        if arr[y][x] > max:
            max = arr[y][x]
            max_y = y
            max_x = x
        elif arr[y][x] < min:
            min = arr[y][x]
            min_y = y
            min_x = x
print(f'MAX={max}({max_y},{max_x})')
print(f'MIN={min}({min_y},{min_x})')