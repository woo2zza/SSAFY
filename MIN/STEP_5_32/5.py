import sys
sys.stdin = open("input.txt", "r")
lst = []
N = int(input())
for i in range(N):
    lst.append(input())
arr = sorted(lst, key= lambda x : (len(x),x) )
for i in arr:
    print(i)