arr1 = [2,1,2,4,5]
arr2 = [[2,5,3],[4,5,7],[8,7,2]]

num = int(input())

count1 = 0
for i in arr1:
    if i == num:
        count1 += 1

count2 = 0
for j in arr2:
    for k in j:
        if k ==num:
            count2 += 1

print(count2)