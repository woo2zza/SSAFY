arr = []
star = []
for i in range(3):
    st = input()
    arr.append(len(st))
    star.append(st)

max_len = max(arr)

for j in range(len(star)):
    if max_len == len(star[j]):
        print(star[j])   