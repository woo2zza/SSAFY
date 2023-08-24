import sys
sys.stdin = open('input.txt','r')
x, y = map(int, input().split())
arr = [0]
arr2 = [0]

cut = int(input())
for i in range(cut):
    cutx, cuty = map(int, input().split())
    if cutx == 0:
        arr.append(cuty)
    elif cutx == 1:
        arr2.append(cuty)

arr.append(y)
arr2.append(x)
arr.sort()
arr2.sort()
arr_Max = -2e15
arr2_Max = -2e65
for i in range(1, len(arr)):
    A = arr[i] - arr[i-1]
    if A > arr_Max:
        arr_Max = A

for i in range(1, len(arr2)):
    B = arr2[i] - arr2[i-1]
    if B > arr2_Max:
        arr2_Max = B

print(arr_Max * arr2_Max)
print(arr)
print(arr2)