num = list(map(int, input().split()))
count = 0
for i in num:
    if 3 <= i <= 7:
        count += 1
print(count)