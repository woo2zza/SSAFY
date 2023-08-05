arr = ['A','T','K','P','T','C','A','B','C']
A,B = list(input().split())

inx = 0
iny = 0
for i in range(len(arr)):
    if A == arr[i]:
        inx = i
        break
for j in range(len(arr)):
    if B == arr[j]:
        iny = j
        


print(abs(iny - inx))
