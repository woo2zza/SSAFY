a = list(map( int,input().split()))
arr = []
for i in a:
    arr.append(i+2)

for j in range(0,6,2):
    print(arr[j],arr[j+1])
