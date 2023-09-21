def find(x):
    if parents[x] == x:
        return x
    else:
        ret = find(parents[x])
        parents[x] = ret
        return ret


def union(v,w,A):
    resultA , resultB = find(v), find(w)
    if resultA == resultB:
        return
    else:
        if A[resultA] > A[resultB]:
            parents[resultA] = resultB
        else :
            parents[resultB] = resultA


N, M, K = map(int, input().split())
parents = [ x for x in range(N+1)]
A = [0] + list(map(int, input().split()))
for i in range(M):
    v, w = map(int, input().split())
    union(v,w,A)


ans = 0
for idx, root in enumerate(parents):
    if idx == root:
        ans += A[idx]

if ans <= K:
    print(ans)
else:
    print("Oh no")