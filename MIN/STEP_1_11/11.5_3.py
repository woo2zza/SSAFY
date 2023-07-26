arr = ['A','1','1','1','5','A','w','z']

st = input()
count = 0
for i in arr:
    if st == i:
        count += 1

if count >= 3 :
    print('THREE')
elif count == 2:
    print('TWO')

elif count == 1:
    print('ONE')
else:
    print('NOTHING')