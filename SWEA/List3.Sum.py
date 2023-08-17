
for q in range(1, 11):
    a = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    Max_arr = []
    for i in range(100):
        Max = 0
        Max2 = 0
        for j in range(100):
            Max += arr[i][j]
            Max_arr.append(Max)
            Max2 += arr[j][i]
            Max_arr.append(Max2)
    Max3 = 0
    for i in range(100):
        Max3 += arr[i][i]
        Max_arr.append(Max3)

    print(f'#{a} {max(Max_arr)}')