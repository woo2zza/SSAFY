arrs = [
    ['D','A','D'],
    ['Q','W','Q'],
    ['A','S','D'],
    ['A','S','D']
]

def find(st):
    for arr in arrs:
        if st in arr:
            print('존재')
            return
        else:
            print('없음')
            return
    

st = input()
find(st)