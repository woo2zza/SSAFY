arr = [0] * 7
integer = map(int, input().split())
a = 0
for i in integer:
    arr[a] = i
    a += 1
print(arr[0] + arr[-1])