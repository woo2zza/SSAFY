def odd():
    arr = [[0]*4 for i in range(4)]
    a = 1
    for x in range(4):     
        arr[x][x] = a
        a+= 1    
    for i in arr:
        print(*i)
    

def even():
    arr = [[0]*4 for i in range(4)]
    a = 1

    b = 3
    for x in range(4):
        for y in range(b,b+1):
            arr[x][y] = a
            a+= 1
        b -= 1
    for i in arr:
        print(*i)
    
num = int(input())
if num % 2 == 0:
    odd()
else:
    even()