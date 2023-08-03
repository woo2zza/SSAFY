def isSame(arr):
    if arr[0] == arr[1]:
        return 1
    return 0


name = [input().split() for _ in range(2)]
ret = isSame(name)
if ret == 1:
    print('동명')
else: print('남남')