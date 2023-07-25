arr = [['D','A','C','C','D'],['S','D','F','A','E'],['E','E','T','J','H']]

def in_fun():
    st = input()
    return st

def check():
    A = in_fun()
    for i in arr:
        for j in i:
            if  A == j:
                return print('있음')
            # else:
            #     print('없음')
    print('없음')


check()