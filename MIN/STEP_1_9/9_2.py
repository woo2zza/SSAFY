arr = [['A','B','C','D','E'],['E','A','B','A','B'],['A','C','D','E','R']]
A = input()
count = 0
for i in arr:
    for j in i:
        if j ==A:
            count += 1

if count >= 3:
    print('대발견')
elif count ==1 or count == 2:
    print('발견')

else:
    print('미발견')