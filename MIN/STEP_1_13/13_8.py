def compareGo():
    if arr[i] == arr2[i]:
        print('두배열은완전같음')
    else:
        print('두배열은같지않음')


arr = [3, 5, 1, 2, 7]
arr2 = [0] * 5
number = list(map(int, input().split()))
for i in range(5):
    arr2[i] = number[i]
compareGo()