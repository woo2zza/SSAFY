num = int(input())
arr = [[0]*4 for i in range(3)]

k = 2
for x in range(0,3):
    for y in range(k,4):
        arr[x][y] = num
        num += 1
    k -= 1


for ar in arr:
    for a in ar:
        if a == 0:
            a = ' '
        print(a, end = '')
    print()
        # a[0][2] 
        # a[0][3]

        # a[1][1]
        # a[1][2]
        # a[1][3]

        # a[2][0]
        # a[2][1]
        # a[2][2]
        # a[2][3]