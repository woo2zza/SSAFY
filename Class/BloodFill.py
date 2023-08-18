from collections import deque
N = int(input())
arr = [[0] * N for _ in range(N)]
arr[2][1] = 1
endy, endx = map(int, input().split())

# 2,1 좌표가 1인 배열 선언, 만날 좌표 선언
directy = [0 ,0, 1, -1]
directx = [1 ,-1, 0 ,0]

# 2,1 의 주변으로 갈 direct 배열 선언
dequ = deque()
dequ.append((2,1))

# dequ라는 데큐 만들고 초기값인 2,1 으로 넣어줌

while dequ:
    # deqy 데크가 존재할때까지 while 구문 반복
    movey, movex = dequ.popleft()
    # movey, movex에 dequ에 있던 원소 넣기
    for i in range(4):
        dx = movey + directy[i]
        dy = movex + directx[i]
        # dequ에 있었던 초기값의 주변에 있는 모든 값을 확인 후 dequ에 넣기
        if dx > N-1 or dx < 0 or dy > N -1 or dy < 0: continue
        if arr[dy][dx] != 0: continue
        dequ.append((dy, dx))
        # dy, dx가 범위 밖이거나 0이 아니면(한번 거쳤던 곳이면) 제외
        arr[dy][dx] = arr[movey][movex] + 1
        # dy, dx에 전의 값인 movey, movex 의 값에 + 1 한 값을 넣어줌
        if arr[dy][dx] == arr[endy][endx]:
            print(arr[endy][endx])

for i in arr:
    print(i)

