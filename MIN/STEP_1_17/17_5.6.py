arr = [3, 7,4, 9]
def Input(arr2):
    if arr == arr2:
        return f'pass'
    else:
        return f'fail'


arr2 = list(map(int, input().split()))
ret = Input(arr2)
print(ret)