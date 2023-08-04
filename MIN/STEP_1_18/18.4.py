card = list(input())
bucket = [0] * 15
for i in range(len(card)):
    bucket[ord(card[i])-65] = 1
print(f'{sum(bucket)}개')
