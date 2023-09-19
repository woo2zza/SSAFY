import heapq
st = list(input())


heap = list(map(lambda x: -ord(x) , st))
heapq.heapify(heap)
for i in range(len(heap)):
    print(chr(-heapq.heappop(heap)), end ='')