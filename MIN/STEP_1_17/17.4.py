arr = [['A','T','K','B'],
       ['C','Z','F','D'],
       ['H','G','E','I']]


def find(st):
    find = 0
    for i in range(3):
        for j in range(4):
            if arr[i][j] == st[0]:
                find = arr[i + int(st[1])][j + int(st[2])]
    return find


st = list(input().split())
ret = find(st)
print(ret)