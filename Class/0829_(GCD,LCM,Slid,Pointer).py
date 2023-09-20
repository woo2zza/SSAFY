# num1, num2 = map(int, input().split())
#
# answer = 0
# for i in range(2, min(num1, num2) +1):
#     if num1 % i == 0 and num2 % i == 0:
#         answer = i
# print(answer)

print(' 유클리드 호세법 ')

# num1, num2 = map(int, input().split())
# while num2:
#     temp = num1 % num2
#     num1 = num2
#     num2 = temp
# print(num1)

print('소수구하기_ 기본코드')
# num = int(input())
# ans = [2]
# for i in range(2, num +1):
#     flag = 0
#     for j in range(2, i):
#         if i != j and i%j == 0:
#             flag = 1
#             break
#         if flag == 0: ans.append(i)
# print(*set(ans))

print('소수구하기_에라토스테네스의 체')
# import math
# num = int(input())
# end = int(math.sqrt(num))
# check = [0] * (num+1)
# for i in range(2, end+1):
#     if check[i] == 1: continue
#     for j in range(i + i, num + i, i):
#         check[j] = 1
#
# for i in range(2, num +1):s
#     if check[i] == 0: print(i, end = ' ')
print('sliding window')
# 연속된 구간의 합
arr = list(map(int, input().split()))
N = int(input())
Sum = sum(arr[0:N])
lst = [Sum]
for i in range(len(arr) - N):
    Sum = Sum - arr[i] + arr[i+N]
    lst.append(Sum)
print(max(lst))
