arr = [list(map(int, input().split())) for _ in range(4)]
lst = []
pp = 0
row = col = 0
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            pp = arr[i][j]
            row =  i
            col = j
            lst.append((i,j))
print(str(lst[0]).replace(' ',''))
print(str(lst[-1]).replace(' ',''))