lst = [0,1,2,3,4,5]
arr = [
    [2,3,5],
    [3,4,5],
    [4,5],
    [],
    [0,5],
    []
]
used = [0] * 6
st = int(input())
def abc(now):
    print(now, end = ' ')
    for i in arr[now]:
        if used[i] == 1: continue
        used[i] = 1
        abc(i)
used[st] = 1        
abc(st)