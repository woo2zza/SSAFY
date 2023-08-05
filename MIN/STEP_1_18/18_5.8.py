st = [list(input()) for _ in range(3)]

bucket = [0] * 26
for i in range(3):
    for j in range(len(st[i])):
        bucket[ord(st[i][j]) - 65] += 1

Flag = True
for i in range(len(bucket)):
    if bucket[i] >= 2:
        Flag = False
        break
if Flag: print('Perfect')
else: print('No')