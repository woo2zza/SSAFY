arr= [0] * 4
num = list(map(int, input().split()))
sum = 0
for i in range(4):
    arr[i] = num[i]
    sum += arr[i]
print(sum)
