import sys
sys.stdin = open("input.txt","r")
N,M = map(int, input().split())
lst = []
for i in range(M):
    lst.append(input().split())

Max = 0
idx = 0
arr = sorted(lst, key= lambda x:x[0])
bucket = [0] * M
for i in range(len(arr)):
    bucket[int(arr[i][0])] += 1
for i in range(len(bucket)):
    if Max < bucket[i]:
        Max = bucket[i]
        idx = i
for i in range(len(arr)):
    if arr[i][0] == str(idx):
        print(arr[i][1], end = ' ')