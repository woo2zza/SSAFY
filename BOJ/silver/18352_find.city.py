import heapq
N, M, K, X = map(int, input().split())
lst = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    lst[A].append((B,1))

inf = int(32e10)
result = [inf] * N

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (start, 0))
    result[start] = 0


    while heap:
        C, D  = heapq.heappop(heap)

        if D > result[C]:continue

        for i in lst[D]:
            road = C + i[1]
            if road  < result[i[0]]:
                result[i[0]] = road
                heapq.heappush(heap, (road, i[0]))

dijkstra(X)
print(result)