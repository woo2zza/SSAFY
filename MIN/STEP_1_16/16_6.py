num = list(map(int, input().split()))
arr = []
Sum = 0
for i in range(len(num)):
    Sum += num[i]
    arr.append(Sum)
print(*arr)