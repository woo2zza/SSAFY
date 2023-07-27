arr = [
    [1, 0, 0, 0 ,0],
    [1 ,0 ,1 ,0 ,0],
    [1, 1, 0 ,1, 0],
    [1 ,0 ,1 ,0 ,0],
    [0, 1, 0, 0, 1],
    [0 ,0 ,0 ,1 ,0],
    [1 ,1 ,0 ,0 ,0]
]

def in_fu():
    num = int(input())
    return num

def process():
    count = 0
    A =in_fu()
    for j in range(7):
        if arr[j][A] == 1:
           count += 1
    return print(count)

process()