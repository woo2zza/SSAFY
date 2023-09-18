lst = []
for i in range(10):
    num = int(input())
    lst.append(num%42)
bucket = [0] * 200
for i in lst:
    bucket[i]  = 1

print(sum(bucket))