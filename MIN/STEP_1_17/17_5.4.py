arr = [['G','K','T'],['P','A','C']]

def find(st):
    for ar in arr:
        for a in ar:
            if a == st:
                return 1
    return 0

st = list(input().split())
Sum = 0
for i in st:
    ret = find(i)
    print(ret)

if Sum == 2: print('대발견')
elif Sum == 1: print('중발견')
else: print('미발견')
