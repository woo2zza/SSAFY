st = list(input())
def find(st):
    mid = len(st) // 2
    if st[:mid] == st[mid:]:
        print('동일한문장')
    else:
        print('다른문장')


find(st)