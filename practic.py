while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    if lst[0] ** 2 + lst[1] **2 == lst[2] **2:
        print('right')
    else:
        print('wrong')