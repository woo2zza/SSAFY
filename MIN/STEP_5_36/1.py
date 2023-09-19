import heapq
import sys
sys.stdin = open('input.txt','r')

N, T = map(int, input().split())
lst = [[] for _ in range(N)]

for _ in range(T):
    a,b,w = map(int, input().split())
    lst[a].append((b,w))

inf = int(32e10)
result = [inf] * N

for i in lst:
    print(*i)

def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,0)) #비용 , #노드
    result[start] = 0

    while heap:
        A, B = heapq.heappop(heap)

        for i in lst[B]:
            cost = A + i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(0)
if result[N-1] == inf:
    print('impossible')
else:
    print(result[N-1])