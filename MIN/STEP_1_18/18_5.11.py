st = input()
arr = ['G','H','O','S','T']
def find(i):
    if i in st:
        return 1
    return 0

ar = []
for i in arr:
    ar.append(find(i))

if 0 in ar: print('존재하지 않음')
else: print('존재')