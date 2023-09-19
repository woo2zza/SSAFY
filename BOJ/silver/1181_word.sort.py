N = int(input())
lst = []
for i in range(N):
    lst.append(input())
new = list(set(lst))
print(new)

ret = sorted(new, key = lambda x:(len(x), x))
for i in ret:
    print(i)
print(ret)