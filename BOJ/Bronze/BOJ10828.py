num = int(input())
lst = []
for i in range(num):
    st = input()
    if st == 'top' :
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif st == 'size':
        print(len(lst))
    elif st == 'empty':
        if not lst:
            print(1)
        elif len(lst) > 0:
            print(0)
    elif st == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            A = lst.pop()
            print(A)
    else:
        lst.append(st[5:])
