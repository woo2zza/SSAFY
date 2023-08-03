arr = [3, 7, 4, 1, 2, 6]
def find(num):
    for i in arr:
        if i == num:
            return f'OK '
    return f'NO '


univer = [list(map(int, input().split())) for _ in range(2)]
for arr2 in univer:
    for ar in arr2:
        ret = find(ar)
        print(ret, end = '')
    print()
