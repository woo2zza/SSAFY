arr = [0] *4
num1, num2 = map(int, input().split())
arr[0] = num1
arr[2] = num2
print(*arr, sep = '')