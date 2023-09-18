test = int(input())

for i in range(1, test+1):
    num = int(input())
    lst = list(map(int, input().split()))
    Max = max(lst)
    Min = min(lst)
    print(f'#{i} {Max - Min}')
