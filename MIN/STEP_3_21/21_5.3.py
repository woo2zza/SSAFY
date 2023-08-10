st = list(input())
A, B = input().split()
for i in range(1,len(st)-1):
    if st[i] == A or st[i] == B:
       st[i-1] = '#'
       st[i+1] = '#'
if st[0] == A or st[0] == B:
    st[i+1] = '#'
elif st[-1] == A or st[-1] == B:
    st[-2] = '#'
print(''.join(st))