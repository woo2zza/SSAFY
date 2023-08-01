arr = []
for i in range(3):
    st = list(input())
    arr.append(st)


for ar in arr:
    Flag = False
    if 'M' in ar:
        Flag = True
        break

if Flag == 1:
    print('M이 존재합니다')
else:
    print('M이 존재하지 않습니다')