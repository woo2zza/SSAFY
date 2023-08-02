arr = [[3,5,9],
       [4,2,1],
       [5,1,5]]

def find(num):
    Flag = False
    for i in range(3):
        for j in range(3):
            if arr[i][j] == num:
                Flag = True


    if Flag : return f'{num}:존재'
    else: return f'{num}:미발견'

num = list(map(int, input().split()))
for i in num:
    ret = find(i)
    print(ret)