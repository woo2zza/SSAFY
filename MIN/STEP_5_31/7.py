num = int(input())
lst = []
for i in range(num):
    lst.append(input())
new = sorted(lst, key = lambda x : (len(x),x))
for i in new:
    print(i)