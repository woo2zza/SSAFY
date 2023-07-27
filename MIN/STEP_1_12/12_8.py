arrs=['D','A','T','A','P','O','W','E','R']
arr2=[]
a, b = map(int, input().split())
for i in range(a,b + 1):
    arr2.append(arrs[i])
print(*arr2, sep = '')
    