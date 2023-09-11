# import sys
# input = sys.stdin.readline
# T = int(input())
# for q in range(T):
#     N, M = map(int, input().split())
#     for i in range(M):
#         a, b = map(int, input().split())
#     print(N-1)

def find(x):
    global parent
    if parent[x] == -1:
        return x
    
    ret = find(parent[x])
    parent[x] = ret
    return ret


def union(a, b):
    
    global parent, cnt
    finda, findb = find(a), find(b)
    if finda == findb:
        return 
    else:
        parent[finda] = findb
    

N, M = map(int, input().split())
parent = [-1] *(N+1)
for i in range(M):
    first, a, b = map(int, input().split())
    if first == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else: 
            print('NO')
