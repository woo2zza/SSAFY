num = list(map( int, input().split()))
for i in range(-1,-7,-1):
    print(num[i], end = ' ')
    if num[i] == 7:
        break