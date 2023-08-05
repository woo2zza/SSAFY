st = list(input())
bucket = [0] * 26
for i in range(len(st)):
    bucket[ord(st[i]) - 65] += 1
for i in range(len(bucket)):
    if bucket[i] >= 1:
        print(f'{chr(i+65)}:{bucket[i]}')