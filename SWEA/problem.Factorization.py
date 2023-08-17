N = int(input())
num = [2, 3, 5, 7, 11]
number = []
for i in num:
    cnt = 0
    while N % i == 0:
        cnt += 1
        N = N / i
    number.append(cnt)
print(f'#{q}', end=" ")
print(*number, sep=" ")