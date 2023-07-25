arr = [3, 5, 2, 4, 1]
arr2 = [[9, 8],[7, 1],[3, 4]]
num = int(input())
if num % 2 == 1:
    for i in arr:
        print(i,end = '')
else:
    for j in arr2:
     print(*j,  sep = '')