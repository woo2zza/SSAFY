
num = list(map(int, input().split()))
number = int(input())
for i in range(3):
    num.append(number + i)
print(*num)
