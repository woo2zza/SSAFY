def arr(num):
    max_val = num[0]
    min_val = num[0]
    max_i, max_j = 0, 0
    min_i, min_j = 0, 0

    lst = [[0]*3 for i in range(2)]

    for i in range(3):
        lst[0][i] = num[i]
        lst[1][i] = num[i+3]

    for i in range(2):
        for j in range(3):
            if lst[i][j] > max_val:
                max_val = lst[i][j]
                max_i,max_j = i,j
            if lst[i][j] < min_val:
                min_val = lst[i][j]
                min_i,min_j =i,j

    return (max_i,max_j),(min_i,min_j)

num = list(map(int, input().split()))
ret_max,ret_min = arr(num)
print(str(ret_max).replace(' ',''))
print(str(ret_min).replace(' ',''))