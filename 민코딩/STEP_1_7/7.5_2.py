arr = [0] * 6
num = list(map(int, input().split()))
for i in range(len(num)):
    arr[num[i]] = 1
print(*arr)