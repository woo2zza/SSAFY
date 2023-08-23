import sys
sys.stdin = open('input.txt')

arr = [[0]*1001 for _ in range(1001)]
paper = int(input())
num = 1
lst = []
for i in range(paper):
    x,y,plusx,plusy = map(int, input().split())
    for j in range(x, x+plusx):
        for k in range(y,y+plusy):
            arr[j][k] = num
    num += 1

for q in range(1, paper+1):
    count = 0
    for i in range(1002):
        for j in range(1002):
            if arr[i][j] == q:
                count += 1

    print(count)
