arr = [[],[]]
num = list(map(int, input().split()))

arr[0]=num[:3]
arr[1]=num[3::]

Max = 0
Min = 0
in_Max = 0
in_Min = 0
for x in range(2):
    for y in range(3):
        if arr[x][y] > Max:
            Max = arr[x][y]
            in_Max = x, y
        elif arr[x][y] < Min:
            Min = arr[x][y]
            in_Min = x, y
print(f'({in_Max[0]},{in_Max[1]})')
print(f'({in_Min[0]},{in_Min[1]})')
