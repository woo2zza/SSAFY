def isExist(arr):
    st = input()
    Flag = False
    for i in range(4):
        if arr[i] == st:
            Flag = True
    if Flag == True:
        return f'발견'
    else: return f'미발견'
arr = ['M','T','K','C']
ret = isExist(arr)
print(ret)