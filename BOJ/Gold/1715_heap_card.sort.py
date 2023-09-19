import heapq
import  sys
sys.stdin = open('input.txt', 'r')
heap = []
N = int(input())
for i in range(N):
    heapq.heappush(heap, int(input()))


Sum = 0
while len(heap) > 1:
    temp1 = heapq.heappop(heap)
    temp2 = heapq.heappop(heap)
    Sum += (temp1 + temp2)
    heapq.heappush(heap, (temp1 + temp2))
print(Sum)