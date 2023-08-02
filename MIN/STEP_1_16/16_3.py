# def arr(num):
#     in_max,in_max2 = 0 ,0
#     in_min, in_min2 = 0 ,0
#     Max = -20e21
#     Min = 20e5
#     lst = [[0]*3 for i in range(2)]
#     for i in range(3):
#         lst[0][i] = num[i]
#         lst[1][i] = num[i+3]

#     for i in range(2):
#         for j in range(3):
#             if lst[i][j] > Max:
#                 in_max, in_max2 = i, j
#             if lst[i][j] < Min:
#                 in_min ,in_min2 = i, j
#     return f'{in_max,in_max2} \n {in_min,in_min2}'

# num = list(map(int, input().split()))
# ret = arr(num)
# print(ret)

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
print(ret_max, sep = '')
print(ret_min)