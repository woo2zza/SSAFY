arr = [5 ,9, 4, 6, 1, 5, 8, 9]
a, b = map(int, input().split())
count = 0
for i in range(a, arr.index(b)):
    count += 1
print(count)