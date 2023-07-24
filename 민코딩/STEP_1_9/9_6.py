arr= [[],[],[]]

num = 65
for i in arr:
    for j in range(3):
        i.append(chr(num))
        num += 1

a, b = map(int, input().split())
c, d = map(int, input().split())
arr[a][b],arr[c][d] = arr[c][d] , arr[a][b]

for i in arr:
    print(*i, sep = '')