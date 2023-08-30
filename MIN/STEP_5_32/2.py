import sys
sys.stdin = open("input.txt","r")
lst = []
N = int(input())
for i in range(N):
    lst.append((input().split()))

new = sorted(lst, key = lambda x : lst[1])
print(new)