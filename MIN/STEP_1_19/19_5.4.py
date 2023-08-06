arr = [[0]*4 for _ in range(4)]
def fine(st , num):
    for i in range(4):
        if st == 'G': 
            arr[num][i] = 1
        elif st == 'S':
            arr[i][num] = 1
    return arr

for i in range(3):
    a, b = list(input().split())
    b = int(b)
    ret = fine(a, b)
for j in ret:
    print(*j)