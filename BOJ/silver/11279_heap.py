import heapq, sys
input = sys.stdin.readline
sys.stdin = open('input.txt','r')
heap = []

N = int(input())
for i in range(N):
    num = int(input())
    heapq.heappush(heap, -num)

    if num == 0:
        print(-heapq.heappop(heap))

    elif len(heap) == 0:
        print(0)
        break