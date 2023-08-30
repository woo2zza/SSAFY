import sys
sys.stdin = open("../STEP_5_32/input.txt", "r")
lst = []
N = int(input())
for i in range(N):
    lst.append(input().split())

new = sorted(lst, key = lambda x : (x[0], x))

for i in new:
    print(*i)