arr = [[0]*4 for i in range(4)]
a = 1

for x in range(3,-1,-1):
    for y in range(4):
        arr[y][x] = a
        a+= 1
    
for i in arr:
    print(*i)





























# for x in range(3, -1, -1):
#     for y in range(4):
#         arr[y][x] = (4 * x) + y + a

# for i in range(len(arr)):
#     print(*arr[i])