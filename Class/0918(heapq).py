# 우선순위 q
"""
우선순위 q 모듈
import heapq 좀 더 빠름
from queue import PriorityQueue
"""

import heapq

arr = [] # 함수 사용 시 이 리스트를 인자로 넘긴다!!

heapq.heappush(arr, 4)
heapq.heappush(arr, 7)
heapq.heappush(arr, 1)
heapq.heappush(arr, 2)
heapq.heappush(arr, 87)
heapq.heappush(arr, 23)
print(arr) # [1, 2, 4, 7, 87, 23]
# 우선순위 q 에서 default 값은 min heap 이다 0번 인덱스에만 큰 의미가 있다
print(heapq.heappop(arr)) # 1
print(heapq.heappop(arr)) # 2
print(heapq.heappop(arr)) # 4
print(heapq.heappop(arr)) # 7
print(heapq.heappop(arr)) # 23
print(heapq.heappop(arr)) # 87

for i in range(len(arr)):
    print(heapq.heappop(arr), end = ' ')

while arr:
    node = heapq.heappop(arr)
    print(node, end = ' ')


# 오름차순으로 출력하기 (우선순위큐 사용)
import heapq

arr = [234, 56, 234, 1, 45, 456, 23]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, arr[i])

for i in range(len(arr)):
    print(heapq.heappop(heap), end = ' ')

import heapq
arr = [234, 56, 234, 1, 45, 456, 23]
heapq.heapify(arr) #heapify를 이용해서 heap의 자료형으로 바꾸기

for i in range(len(arr)):
    print(heapq.heappop(arr), end = ' ')

# Max heap 으로 바꾸기 방법1

import heapq
arr =[34, 213, 57, 1, 2, 54, 2, 65]
heap = []

for i in range(len(arr)):
    heapq.heappush(heap, -arr[i])

for i in range(len(arr)):
    # print(heapq.heapop(heap) * -1)
    print(-heapq.heapop(heap))

# Max heap으로 바꾸기 방법 1-1
import heapq
arr = [34, 213, 57, 1, 2, 54, 2, 65]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, (-arr[i], arr[i]))

for i in range(len(arr)):
    print(heapq.heappop(heap)[1])

# Max heap으로 바꾸기 방법 2 [추천]
import heapq
arr=[34,213,57,1,2,54,2,65]

heap=list(map(lambda x:-x,arr))
heapq.heapify(heap)

for i in range(len(arr)):
    print(-heapq.heappop(heap),end=' ')

"""
카드 정렬하기

정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.


입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.


출력
첫째 줄에 최소 비교 횟수를 출력한다.

입력
4
50
20
70
30

출력
320


입력
3
10
20
40

출력
100
"""

import heapq

n = int(input())
card = []

for i in range(n):
    heapq.heappush(card, int(input()))

answer = 0
while len(card) > 1:
    temp1 = heapq.heappop(card)
    temp2 = heapq.heappop(card)

    answer += (temp1 + temp2)
    heapq.heappush(card, temp1 + temp2)

print(answer)
