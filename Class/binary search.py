arr = [4,5,7,9,11,15,16,17,18,19, 20]
target = 11

def find(st, ed, target):
    while st <= ed :
        mid = (st + ed) //2
        if arr[mid] == target : return mid
        elif arr[mid] > target : ed = mid -1
        elif arr[mid] < target : st = mid + 1
    return -1

print(find(0, len(arr)-1,target))