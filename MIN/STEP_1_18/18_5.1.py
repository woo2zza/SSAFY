arr = [
    ['G','K','G'],
    [0,0,0]
]
num = input().split()
for i in range(3):
    arr[1][i] = num[i]

bucket = [0] * 21
for i in range(2):
    for j in range(3):
        bucket[ord(arr[i][j])-65] +=1
if max(bucket) >= 3 :
    print('있음')
else: print('없음')