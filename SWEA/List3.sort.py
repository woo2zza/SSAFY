N = int(input())
num = list(map(int, input().split()))
for i in range(N-1):
    for j in range(N-1):
        if num[i] > num[i +1]:
            num[i], num[i+1] = num[i +1] , num[i]
    
print(num)
