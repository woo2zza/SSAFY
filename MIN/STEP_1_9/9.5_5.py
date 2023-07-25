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

def findUpper(C):
    count = 0
    for i in C:
        for j in i:
            if 65 <= ord(j) <= 90:
                count += 1
    return print(f'대문자{count}개')

def findLower():
    B = in_fun()
    findUpper(B)
    count2 = 0
    for i in B:
        for j in i:
            if 97 <= ord(j) <= 122:
                count2 += 1
    return print(f'소문자{count2}개')



findLower()