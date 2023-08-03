num = int(input())
i = 1
count = 1
while  num > i:
        i += 6 * i
        count += 1
        i += 1
print(count)