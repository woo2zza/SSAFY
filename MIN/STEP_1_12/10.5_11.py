def run():
    arr = [[0]*3 for i in range(3)]
    A = 1
    for i in range(3):
        for j in range(3):
            arr[i][j] = A
            A += 1
    return arr

def run2():
    arr2 = [[0]*3 for i in range(3)]
    B = 1
    for x in range(3):
        for y in range(2,-1,-1):
            arr2[x][y] = B
            B += 1
    return arr2


num = int(input())
if num < 10:
    ret = run()
    for i in ret:
        print(*i, sep = '')

else :
    ret2 = run2()
    for j in ret2:
        print(*j, sep = '')