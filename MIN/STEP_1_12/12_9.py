arrs = [[0]*3 for i in range(3)]
arrss = [[0]*3 for i in range(3)]

st = input()
if '0' <= st <= '9':
    num = 6
    k = 0
    for x in range(0,3):
        for y in range(k,3):
            arrs[x][y] = num
            num -= 1
        k += 1


    for arr in arrs:
        for ar in arr:
            if ar == 0:
                ar = ' '
            print(ar, end = '')
        print()

else:

    number = 1
    e = 3
    for x in range(2,-1,-1):
        for y in range(0, e):
            arrss[x][y] = number
            number += 1
        e -= 1

    for arr in arrss:
        for ar in arr:
            if ar == 0:
                ar = ' '
            print(ar,end = '')
        print()