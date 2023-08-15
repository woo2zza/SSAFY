lst = ['A','B','C','D','E','F','G','H']
arr = [
    [0 ,1 ,1, 0 ,0 ,0 ,0 ,1],
    [0, 0 ,0, 0 ,0 ,0 ,0 ,0],
    [0, 0, 0 ,1 ,1 ,0 ,1 ,0],
    [0 ,0 ,0 ,0 ,0 ,1 ,0 ,0],
    [0 ,0 ,0 ,0 ,0, 0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0, 0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
    [0, 0 ,0 ,0 ,0 ,0 ,0 ,0]
]
st = input()
idx = -1
idy = -1
for i in range(len(lst)):
    if st == lst[i]:
        idx = i
        break
if idx == 0:
     print('없음')
for j in range(8):
    if arr[j][idx] == 1:
        idy = j
for k in range(8):
    if arr[idy][k] == 1 and lst[k] != st:
        print(lst[k], end = ' ')



    # for i in range(6):
    #       if arr[parents][i]==1 and i!=idx:
    #            bro=i
    #            break
    # if bro==-1:
    #       print('형제 없음')
    # else:
    #       print(chr(i+ord('A')))