check = int(input())
dump = list(map(int, input().split()))
Max = 0
Min = 0
for j in range(check):
    for i in range(len(dump)):
        if dump[i] > Max:
            Max = dump[i]
            Max -= 1
        if dump[i] < Min:
            Min = dump[i]
            Min += 1

    print(Max , Min)