arr = [2,3,4,5,1,2,5,9]
result = [0] *8

end = 7
start = 0
mid = (start + end ) // 2
b = mid + 1
a = mid -1
index = 0

while 1:
    if a > mid and  b > end : break

    if a > mid:
        result[index] = arr[b]
        index += 1
        b+= 1

    elif b > end :
        result[index] = arr[a]
        index += 1

    elif arr[a] < arr[b]:
        result[index] = arr[a]
        index += 1
        a += 1

    else:
        result[index] = arr[b]
        index += 1
        b += 1

