arr = []
num, num1 = map(int, input().split())
arr.append(num)
arr.append(num1)
for i in range(4):
    arr.append(arr[i] * arr[i+1]) 
# arr.append(arr[1] * arr[2])
# arr.append(arr[2] * arr[3])
# arr.append(arr[3] * arr[4])
print(arr[-1])