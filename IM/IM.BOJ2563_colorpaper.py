paper = int(input())
arr = [[0]*100 for _ in range(100)]
for q in range(paper):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y + 10):
            arr[i][j] = 1

count = 0
for i in arr:
    for j in i:
        if j == 1:
            count += 1
print(count)