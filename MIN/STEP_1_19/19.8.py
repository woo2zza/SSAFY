arr = [list(map(int, input().split())) for _  in range(4)]

def find(x, y):
    Sum = 0
    for i in range(2):
        for j in range(3):
            dx = x + i
            dy = y + j
            Sum += arr[dx][dy]
    return Sum
Max = 0
indx = 0
indy = 0
for i in range(3):
    for j in range(2):
        ret = find(i, j)
        if ret > Max:
            Max = ret
            indx = i
            indy = j
print(f'({indx},{indy})')