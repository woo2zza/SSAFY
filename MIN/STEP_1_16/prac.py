

arr = [4 ,7 ,1 ,3 ,5]

for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)