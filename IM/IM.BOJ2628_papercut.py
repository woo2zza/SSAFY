import sys
sys.stdin = open('input.txt','r')
x, y = map(int, input().split())
arr = [[0] * x for _ in range(y)]

cut = int(input())
for i in range(cut):
    cutx, cuty = map(int, input().split())
    if cutx == 0:
        arr[cuty].insert(0,[1]*x)
    elif cuty == 0:
        arr[cutx].insert(0,[1]*y)

for i in arr:
    print(i, sep = ' ')