import heapq
arr =[34, 213, 57, 1, 2, 54, 2, 65]
heap = []

for i in range(len(arr)):
    heapq.heappush(heap, arr[i])

for i in range(len(heap)):
    print(heapq.heappop(heap), end = ' ')