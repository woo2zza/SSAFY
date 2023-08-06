arr = [['A', 'B', 'G', 'K'],
       ['T', 'T', 'A', 'B'],
       ['A', 'C', 'C', 'D']]

patten =[]
for i in range(2):
    patten.append(list(input()))

def finding(a, b):
    for i in range(2):
        for j in range(2):
            if patten[i][j] != arr[a + i][b + j]:
                return 0
    return 1


cnt = 0
for row in range(2):
    for col in range(3):
        ret = finding(row, col)
        if ret:
            cnt = 1
if cnt > 0:
    print(f'발견({cnt}개)')
else:
    print('미발견')
