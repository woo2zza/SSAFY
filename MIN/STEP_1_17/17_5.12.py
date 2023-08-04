arr = [[0] * 5 for _ in range(5)]
alpha = 65
for x in range(5):
    for y in range(5):
       arr[x][y] = chr(alpha)
       alpha += 1

st = input()
inx = 0
iny = 0
for x in range(5):
    for y in range(5):
        if arr[x][y] == st:
            inx, iny = x, y

print(f'{inx-2},{iny-2}')



