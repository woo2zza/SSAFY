arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
a = 3
for i in range(4):
    print((arr1[i] + arr2[a]), end = ' ')
    a -= 1