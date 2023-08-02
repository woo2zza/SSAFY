arr = [[0, 0, 1 ,0, 0],
       [0, 0 ,1, 1 ,1]]

arr2 = [[3, 5, 4 ,1 ,1],
        [3, 5, 2 ,5 ,6]]

num = int(input())
Flag = 0
for i in range(2):
    for j in range(5):
        if arr2[i][j] == num and arr[i][j] == 1:
            Flag = True

if Flag == True:
    print(f'{num} 존재')
else:
    print(f'{num} 없음')

