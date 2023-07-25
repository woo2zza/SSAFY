num = int(input())
lst = []
for i in range(num):
    A, B = map(int, input().split())
    lst.append(A+B)
for j in lst:
    print(j)