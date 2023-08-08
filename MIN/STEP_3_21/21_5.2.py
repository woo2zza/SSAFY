arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6]
]
Sum = []

num = int(input())
for i in range(4):
    multi = 0
    for j in range(3):
        multi += arr[j][i]
    Sum.append(multi)
print(Sum)