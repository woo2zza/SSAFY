arr = [[0] * 255 for _ in range(1000)]
num = int(input())
floor = list(map(int, input().split()))
for x in range(2, 1001):
    for y in range(len(floor)):
        arr[x][y] = floor[y]

print(arr)