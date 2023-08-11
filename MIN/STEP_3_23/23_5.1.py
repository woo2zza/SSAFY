arr = [3,5,1,9,7]
for i in range(4):
    st = input()
    if st =='R':
        arr = arr[-1:] + arr[:4]

    elif st == 'L':
        arr = arr[1:] + [arr[0]]
print(*arr)