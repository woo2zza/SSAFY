arr = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]
def getsum(n):
    Sum = 0
    for i in range(5):
        Sum += arr[n + i]
    return Sum

num = int(input())
ret = getsum(num)
print(ret)