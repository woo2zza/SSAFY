arr = [[4, 3, 1, 1],[3, 1,2,1],[0, 0, 1, 2]]
num = int(input())
count = 0
for i in arr:
    for j in i:
        if num == j:
            count += 1
print(f'{count}개 존재합니다')