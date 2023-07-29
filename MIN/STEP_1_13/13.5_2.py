arr = [4,2,5,1,6,7,3]
alpa1, alpa2 = input().split()
alp1_ord , alp2_ord = (ord(alpa1) - 65), (ord(alpa2) -65)
sum_length = 0
if alp1_ord > alp2_ord:
    alp1_ord, alp2_ord = alp2_ord, alp1_ord
for i in range(alp1_ord+1, alp2_ord):
    sum_length += arr[i]
print(sum_length)
