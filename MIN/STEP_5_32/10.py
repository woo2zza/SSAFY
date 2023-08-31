import sys
sys.stdin = open("input.txt","r")
ret = []
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst2 = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if lst2[i][j] == 1:
            ret.append(lst[i][j])

result = sorted(ret, key= lambda x : (-ret.count(x), x))
print(*result)