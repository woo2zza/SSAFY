arr = [
    [4 ,5 ,7 ,1 ,3 ,2],
    ['D','F','Q','W','G','Z']
]
num = int(input())
for x in range(6):
    if arr[0][x] == num:
        print(arr[1][x])
