N = int(input())
lst = list(map(int, input().split()))
bucket = [0] * 10
for i in range(len(lst) - 2):
    if lst[i] == lst[i+1] == lst[i+2]:
        lst[i] = 0
        lst[i+1] = 0
        lst[i+2] = 0
new = sorted(lst, key = lambda x : x)
for i in new:
    if i>0:
        print(i, end = ' ')
