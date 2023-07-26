big_arr = []
small_arr = []
arr = [0]*8
st = list(input().split(sep = ''))
for i in range(8):
    arr[i] = st[i]


for i in st:
    if 65 <= ord(i) <= 90:
        big_arr.append(i)
    else:
        small_arr.append(i)


print(f"big={''.join(big_arr)}")
print(f"small={''.join(small_arr)}")

