num = int(input())
n = list(map(int, input().split()))

lst = []
Sum = sum(n[:4])

for i in range(num - 4):
    Sum = Sum + n[4+i] - n[i]
    lst.append(Sum)
print(min(lst))