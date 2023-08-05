arr = list(map(int, input().split()))
bucket = [0] * 10
for i in arr:
    bucket[i] += 1
if max(bucket) >=2 :
    print('도플갱어 발견')
else: print('미발견')