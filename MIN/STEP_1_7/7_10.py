
def input_arr():
    arr = [[],[],[],[]]
    char = input()
    for i in range(4):
        a=[0,0,0,0]
        for j in range(4):
            a[j] = char
        arr[i] = a
    return arr

a = input_arr()
for i in a:
    print(*i, sep = '')
