name = ['Amy','Bob','Edger','Diane','Chloe']
arr = [[0, 0 ,1 ,0 ,0],
       [1 ,0, 0, 0 ,0],
       [0, 0 ,0 ,0 ,0],
       [0 ,1 ,0 ,0 ,0],
       [0, 1, 0 ,0 ,0]]

Max = -25
idx = 0
for i in range(5):
    Sum = 0
    for j in range(5):
        Sum += arr[j][i]
        if Max < Sum:
            Max = Sum
            idx = i

print(name[idx])