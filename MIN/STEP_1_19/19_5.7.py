arr = [[3,5,1],
       [3,8,1],
       [1,1,5]]
Max = 0
arr2 = [list(map(int, input().split())) for _ in range(2)]
def find(x, y):
    Sum = 0
    for i in range(2):
        for j in range(2):
            if arr2[i][j] == 1:
                Sum += arr[i+x][j+y]
    return Sum

for i in range(2):
    for j in range(2):
       if find(i,j) > Max :
           Max = find(i, j)
           idx = i,j
print(str(idx).replace(' ',''))
     