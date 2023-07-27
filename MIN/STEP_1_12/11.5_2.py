arr = [
    [1, 1, 1],
    [1, 2, 1],
    [3, 6, 3]
]

num = int(input())
count = 0
for i in arr:
    for j in i:
        if j == num:
            count += 1
print(count)