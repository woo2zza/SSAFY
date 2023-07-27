arr = [
    [1, 3, 6, 2],
    [4, 2, 4, 5],
    [6, 3, 7, 3],
    [1, 5, 4, 6]
]
arr2 = []
num = int(input())
for i in arr:
    for j in i:
        if j > num:
          arr2.append(j)

for i in arr2:
   print(i, end = ' ')