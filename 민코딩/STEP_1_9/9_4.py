arr= [3 ,4 ,2, 5, 7, 9]
n1, n2 = map(int, input().split())
arr[n1], arr[n2] = arr[n2], arr[n1]
for i in arr:
    print(i, end = ' ')