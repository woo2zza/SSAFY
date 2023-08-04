st = list(input())
bucket = [0] * 26
Max = 0
Max_in = 0
for i in range(len(st)):
    bucket[ord(st[i])-65] += 1
for i in range(len(bucket)):
    if Max < bucket[i]:
        Max = bucket[i]
        Max_in = i
print(chr(Max_in+65))
