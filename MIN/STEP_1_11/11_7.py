arr = [0]*7
num = list(map(int, input().split()))

for i in range(7):
    arr[i] = num[i]

for j in range(6):
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        pass
print(f'MAX={arr[-1]}')

for j in range(6):
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        pass
print(f'MIN={arr[0]}')


