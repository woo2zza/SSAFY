arr = []
num, num1 = map(int, input().split())
arr.append(num)
arr.append(num1)
for i in range(2,6):
    arr.append(arr[i] * arr[i+1])
print(arr[-1])