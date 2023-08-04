arr = list(map(int, input().split()))
lst = []
for i in range(0,6,2):
    lst.append(arr[i])
Min = 30
for i in lst:
    if Min > i:
        Min = i
print(f'arr[{arr.index(Min)}]={Min}')