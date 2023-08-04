arr = list(map(int, input().split()))
ret = [0] * 4
for i in range(len(arr)):
    if 10 <= arr[i] <= 20: ret[0] += 1
    elif 30 <= arr[i] <= 60: ret[1] += 1
    elif 100 <= arr[i] <= 150: ret[2] += 1
    elif 200 <= arr[i] <= 300: ret[3] += 1
for i in range(4):
    print(f'lev{i}:{ret[i]}')


