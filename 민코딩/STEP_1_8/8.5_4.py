arr = [0] * 17
def in_fun():
    global a
    a, b, c = input().split()
    for i in range(7):
        arr[i] = a
    for i in range(7,13):
        arr[i] = b
    for i in range(13, 17):
        arr[i] = c
    for k in range(16,-1,-1):
        print(arr[k], end = '')

in_fun()