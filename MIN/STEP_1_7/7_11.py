
a=int(input())

lst = []
lst_2 = []

def process():
    global a, lst, lst_2
    for i in range(3):
        for ii in range(3):
            lst_2.append(a)
            a=a+1
        lst.append(lst_2)
        lst_2 = []

def aa():
    global a, lst
    for i in lst:
        for ii in range(3):
            print(i[ii],end=' ')
        print()

process()
aa()