N = int(input())
lst = list(map(int, input().split()))
new = sorted(set(lst))


for i in range(len(new)):
    dict[lst[i]]=new.index(lst[i])
print(dict)