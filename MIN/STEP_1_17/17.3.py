arr = [[3 ,5, 9],
       [4, 2, 1],
       [1, 1, 5]]

def lst(arr2):
       Sum = 0
       for i in range(3):
              for j in range(3):
                     if 1 == arr2[i][j]:
                            Sum += arr[i][j]
       return Sum




arr2 = []
for i in range(3):
       num = list(map(int, input().split()))
       arr2.append(num)

ret = lst(arr2)
print(ret)