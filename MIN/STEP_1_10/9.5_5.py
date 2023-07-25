def in_fun():
    arr = []  
    k = 0
    A = list(input().split())
    for i in range(2):
        arr2 = []
        for j in range(3):    
           arr2.append(A[k])
           k += 1
        arr.append(arr2)      
    return arr

def findUpper(arr):
    count = 0
    for i in arr:
        for j in i:
            if 65 <= ord(j) <= 90:
                count += 1
    return count

def findLower(arr):
    count2 = 0
    for i in arr:
        for j in i:
            if 97 <= ord(j) <= 122:
                count2 += 1
    return count2



findLower()