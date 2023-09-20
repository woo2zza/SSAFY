import heapq
import sys
input = sys.stdin.readline

new = []
N = int(input())

for i in range(N):
    num_list = list(map(int, input().split()))
    if not new:
        for num in num_list:
            heapq.heappush(new, num)
    else:
        for num in num_list:
            if new[0] < num:
                heapq.heappush(new, num)
                heapq.heappop(new)
print(new[0])