import sys
sys.stdin = open("input.txt","r")
arr = [
    ['A','B','C','D'],
    ['A','B','C','E'],
    ['A','G','E','H'],
    ['E','I','E','I'],
    ['F','E','Q','E'],
    ['A','B','A','D']
]

st = list(input())
idx = 0
ret = 0
for i in range(len(st)):
    if st[i] != '?':
        ret, idx = st[i], i
cnt = 0
for i in range(6):
    for j in range(4):
        if arr[i][j] == ret and j == idx:
            cnt += 1
print(cnt)