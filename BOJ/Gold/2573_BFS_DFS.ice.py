# 바다는 0 숫자는 빙산의 높이
# 1년마다 주변 바다의 수 만큼 빙산의 높이가 줄어든다
# 빙산의 높이가 줄어들면 빙산이 쪼개짐
# 빙산이 쪼개졌을 때 몇 년이 걸릴까

# 설계
# 1. 빙산의 개수를 확인하는 배열(lst)을 만들어주고, bfs로 빙산의 개수가 한개임을 확인
# 2. 입력받은 배열(arr)에서 for문으로 0이 아닌 수를 찾는다
# 3. direct배열로 경계선과 for문으로 넘겨준 숫자 주변의 0의 갯수를 찾는다.
# 4. 0의 수만큼 for문으로 넘겨준 숫자에서 차감
# 5. 배열(lst)에서 빙산의 개수가 1개가 아니면 count를 반환

import sys, copy
sys.stdin = open("input.txt","r")
from collections import deque

Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]

directy = [1,-1,0,0]
directx = [0,0,1,-1]

lst = copy.deepcopy(arr)


# 빙산의 개수를 확인
def ice(i, j):
    deq = deque()
    deq.append((i,j))
    lst3[i][j] = 0
    while deq:
        i, j = deq.popleft()
        for q in range(4):
            newi = directy[q] + i
            newj = directx[q] + j
            if newi < 0 or newi > Y-1 or newj < 0 or newj > X-1: continue
            if lst3[newi][newj] == 0:continue
            lst3[newi][newj] = 0
            deq.append((newi,newj))
            
            


# 빙산의 높이 낮추기
def height(i,j):
    for q in range(4):
        newi = directy[q] + i
        newj = directx[q] + j
        if newi < 0 or newi > Y-1 or newj < 0 or newj > X-1: continue
        if lst2[newi][newj] == 0:
            if lst[i][j] > 0:
                lst[i][j] -= 1

# lst는 녹은 빙산 lst2는 녹은 빙산 기준 copy
Flag = 0
count = 0
while Flag == 0:
    lst2 = copy.deepcopy(lst)
    Flag = 1 # 모두0 일 때
    count += 1
    for i in range(Y):
        for j in range(X):
            if lst[i][j] != 0:
                Flag = 0 # 빙산발견 스위치on
                height(i,j)
    
    lst3 = copy.deepcopy(lst) # 빙산의 개수 확인용 복사본
    cnt = 0
    for i in range(Y):
        for j in range(X):
            if lst3[i][j] != 0:
                cnt += 1
                ice(i,j)


    if cnt >= 2:
        print(count)
        exit(0)
   
    
            
print(0)