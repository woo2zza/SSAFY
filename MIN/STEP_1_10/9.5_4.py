arr = [[10,3,20],[60,30,40],[20,30,40]]
a, b = map(int, input().split())
count = 0
for i in arr:
    for j in i:
        if a <= j <= b:
            count += 1
print(count)