bus = int(input())
lst = [1 ,2, 3, 3, 5 ,1, 0 ,1 ,3]
Sum = sum(lst[:bus])

result = []

for i in range(len(lst)-bus):
    Sum = Sum + lst[bus+i] - lst[i]
    result.append(Sum)
print(min(result))