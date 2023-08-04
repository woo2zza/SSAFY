# 1,1 을 기준으로 위 아래 좌 우측에 있는 값들의 합을 출력
# arr = [
#     [3, 5, 4],
#     [1, 1, 2],
#     [1, 3 ,9]
# ]

# y, x = map(int, input().split())
# directy = [-1,1,0,0]
# directx = [0,0,-1,1]
# Sum = 0
# for i in range(4):
#     dy = directy[i] + y
#     dx = directx[i] + x
#     if dx > 2 or dx < 0 or dy > 2 or dy < 0 : continue
#     Sum += arr[dy][dx]
# print(Sum)
#----------------------------------------------------------------
# 입력받은 좌표값의 대각선에 있는 값들의 곱 구하기

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
# x, y = map(int, input().split())
#
# directx = [-1,1,-1,1]
# directy = [-1,1,1,-1]
#
# multi = 1
# for i in range(4):
#     dx = x + directx[i]
#     dy = y + directy[i]
#     if dx > 4 or dx <0 or dy > 4 or dy < 0 : continue
#     multi *= arr[dx][dy]
# print(multi)


# -----------------------------------------------------------
# 위 아래 좌 우로 3칸까지 떨어진 곳들의 합을 구하기

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# x, y = map(int, input().split())
# directx = [-1,1,0,0]
# directy = [0,0,-1,1]
#
# ans = 0
# for i in range(4):
#     for j in range(1,4):
#         dx = x + directx[i] * j
#         dy = y + directy[i] * j
#         if dx < 0 or dy < 0 or dx > 4 or dy > 4: continue
#         ans += arr[dx][dy]
# print(ans)

#------------------------------------------------------------
# 위 아래 좌 우 좌표의 합 중 가장 클 때 max값과 좌표
# arr=[[1,2,3,4],
#      [1,2,9,4],
#      [1,9,3,9],
#      [1,2,9,4]]
#
#
# def isSum(y,x):
#     directy=[0,0,-1,1]
#     directx=[-1,1,0,0]
#     sum=0
#     for i in range(4):
#         dy=directy[i]+y
#         dx=directx[i]+x
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         sum+=arr[dy][dx]
#     return sum
#
# Max=-21e8
# Max_i=0
# Max_j=0
# for i in range(4):
#     for j in range(4):
#         ret=isSum(i,j)
#         if ret>Max:
#             Max=ret
#             Max_i=i
#             Max_j=j
# print(Max,Max_i,Max_j)
#-----------------------------------------------------------
# arr = [[3, 5, 4, 5],
#        [1, 1, 2, 7],
#        [1, 2, 9, 1],
#        [3, 5, 4, 5]]
# sum1 = 0
# sum2 = 0
# for i in range(4):
#     for j in range(4):
#         if i > j:
#             sum1 += arr[i][j]
#         if i < j:
#             sum2 += arr[i][j]
# print(sum1, sum2)

#------------------------------------------------------------

# arr = [[3, 5, 4, 5],
#        [1, 1, 2, 7],
#        [1, 2, 9, 1],
#        [3, 5, 4, 5]]

sum3 = 0
sum4 = 0
for i in range(4):
    sum3 += arr[i][i]
    sum4 += arr[i][3 - i]

print(sum3)
print(sum4)


#--------------------------------------------------------------------
arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

# sum5 에는 1시에서 7시 방향(대각선)으로 합을 구할 시 출력 결과 : 3,6,6,12,21,5,5
n=4
sum5=[0]*(2*n-1)
for i in range(4):
    for j in range(4):
        sum5[i+j] +=arr[i][j]
print(*sum5)





s





