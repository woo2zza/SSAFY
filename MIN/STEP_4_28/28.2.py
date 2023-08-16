n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
idx = 0

for j in range(n):
    if arr[j][0] == 1:
        print(f'boss:{j}')
print('under:',end = '')
for j in range(n):
    if arr[0][j] == 1:
        print(j,end = ' ')
