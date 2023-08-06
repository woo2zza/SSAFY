n = 1
arr = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        arr[i][j] = n
        n +=1
arr2 = [[0]*4 for _ in range(4)]
def fine(num):
    number = 1
    for k in num:
        for i in range(4):
            for j in range(4):
                if arr[i][j] == k:
                    arr2[i][j] = number
                    number += 1
    return arr2
num = list(map(int, input().split()))
ret = fine(num)
for i in ret:
    print(*i)