arr = [
    ['A','B','K','T'],
    ['K','F','C','F'],
    ['B','B','Q','Q'],
    ['T','P','Z','F']
]

def IsStr(st):
    count = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] == st:
                count += 1
    return count




st = list(input().split())
ret1 = IsStr(st[0])
ret2 = IsStr(st[1])
print(ret1 + ret2)