import heapq
import sys
sys.stdin = open("SSAFY/BOJ/Silver/input.txt","r")
N, M, K, X = map(int, input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    lst[A].append((B))

inf = int(32e10)
result = [inf] * (N+1)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    result[start] = 0


    while heap:
        C, D  = heapq.heappop(heap)

        if C > result[D]:continue

        for i in lst[D]:
            road = C + 1
            if road  < result[i]:
                result[i] = road
                heapq.heappush(heap, (road, i))

dijkstra(X)
flag = 0
for i in range(1, N+1):
    if result[i] == K:
        flag = 1
        print(i)
if not flag:
    print(-1)