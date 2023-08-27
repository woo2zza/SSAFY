N, K = map(int, input().split())
num = list(map(int, input().split()))
Sum = sum(num[:K])
lst = [Sum]
 
for i in range(N-K):
    Sum = Sum + num[K+i] - num[i]
    lst.append(Sum)
print(max(lst))