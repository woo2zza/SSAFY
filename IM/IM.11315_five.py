N = int(input())
arr = [list(input()) for _ in range(N)]
new_arr = []
for ar in arr:
    new_arr.append(ar.split('.'))

for i in new_arr:
    print(i)