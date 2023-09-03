def stringLen(A):
    st = list(A)
    count = 0
    for i in st:
        count += 1
    return count



st = input()
A = stringLen(st)
print(f'{A}글자')