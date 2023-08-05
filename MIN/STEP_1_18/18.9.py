arr = [
    [15,18,17],
    [4,6,9],
    [10,1,3],
    [7,8,9],
    [15,2,6]
]
def isPattern(floor):
    for i in range(5):
        if arr[i][0] == floor[0]:
            return 5 - i
        else:
            pass

floor = list(map(int, input().split()))
ret = isPattern(floor)
print(f'{ret}층')