import sys
sys.stdin = open("input.txt","r")

N = int(input())
lst = list(input().split() for _ in range(N))

st , ed = 0, 50

for i in range(len(lst)):
    if lst[i][1] == 'DOWN':
        ed = lst[i][0]
    else:
        st = lst[i][0]
if int(st)+1 == int(ed)-1:
    print(int(st)+1)
elif int(st) < int(ed):
    print(f'{int(st)+1} ~ {int(ed)-1}')
else:
    print('ERROR')