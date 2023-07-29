st = list(input())
count = 0
for s in st:
    count += 1
print(count)

count2 = 0
for s in range(count):
    if st[-1] == st[s]:
        count2 += 1

print(count2)