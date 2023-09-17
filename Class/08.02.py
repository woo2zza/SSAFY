'''
3
1 2 3
4 5 6
7 8 9
'''
di = [0, 1 ,0 ,-1]
dj = [1 ,0 ,-1 ,0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]



max_v = 0  #모든 원소가 0이상이라면..
for i in range(N):  # 모든 원소 arr[i][j]에 대해..
    for j in range(N):
        # s = arr[i][j]
        for k in range(4):
            ni, nj = i +di[k], j + dj[k]
            if 0<=ni<N and 0<=nj<N:         # 배열을 벗어나지 않으면
                s += arr[ni][nj]
            # 여기까지 주변 운소를 포함한 합
        if max_v <s:
            max_v = s

print(arr)