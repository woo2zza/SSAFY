st= list(input())
bucket = [0] * 21
for i in st:
    bucket[ord(i)-65] +=1

Max = 0
indx = 0
for i in range(len(bucket)):
    if bucket[i] > Max:
        Max = bucket[i]
        indx = i
print(chr(indx + 65))