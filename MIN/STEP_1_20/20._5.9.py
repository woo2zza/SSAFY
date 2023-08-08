arr = [
    [3 ,5, 4 ,2, 5],
    [3 ,3, 3 ,2 ,1],
    [3 ,2, 6 ,7 ,8],
    [9, 1, 1 ,3 ,2]
]

A, B = map(int, input().split())
def find(x,y):
    Sum = 0
    for k in range(A):
        for l in range(B):
            Sum += arr[x+k][y+l]
    return Sum
Max = 0
inx = 0
iny = 0
for i in range(4-A+1):
    for j in range(5-B+1):
        ret = find(i,j)

        if ret > Max:
            Max = ret
            inx = i
            iny = j
print(f'({inx},{iny})')