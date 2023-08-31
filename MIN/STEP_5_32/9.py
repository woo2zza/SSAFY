import sys
sys.stdin = open("input.txt","r")
bucket = [0] * 100
lst = list(input())
num = int(input())
arr = sorted(lst, key= lambda x : x[0], reverse= True)
for i in range(num):
    bucket[ord(arr[i])] += 1
Max = idx =  0
for i in range(len(bucket)):
    if Max < bucket[i]:
        Max = bucket[i]
        idx = i

print(chr(idx))