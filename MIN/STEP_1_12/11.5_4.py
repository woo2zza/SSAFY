arr = [
    ['a','b','a','c','z'],
    ['c','t','a','c','d'],
    ['c','c','c','c','a']
]

st = input()
count = 0
for i in arr:
    for j in i:
        if st == j:
            count += 1

if count >= 7:
    print('세상에')
elif count >= 5 :
    print('와우')
elif count >= 3:
    print('이야')
else:
    print('이런')