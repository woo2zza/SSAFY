arr = [[],[],[]]
num = 65
for i in arr:
    a = [0,0,0]
    for j in a:
        a[j] = chr(num)
        num+=1
    arr.append(a)
print(arr)
