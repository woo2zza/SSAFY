import sys
sys.stdin = open("input.txt", "r")
lst = []
for i in range(5):
    lst.append(list(input()))

a, b = map(int, input().split())

arr = sorted(lst[a], key= lambda  x : x)
arr2 = sorted(lst[b], key= lambda  x : x)
lst.remove(lst[a])
lst.remove(lst[b-1])
lst.insert(a, arr)
lst.insert(b, arr2)
print(lst)
for i in range(len(lst)):
    print(lst[i][0], end = ' ')