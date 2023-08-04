arr = [3, 5, 4, 2]
arr2 = list(map(int, input().split()))
Sum = 0
for i in range(len(arr2)):
    if arr2[i] == 1:
        Sum += arr[i]

print(Sum)