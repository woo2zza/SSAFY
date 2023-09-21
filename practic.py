

while 1:
    lst = input()
    if lst == '0': break

    ret = []
    for l in lst:
        ret.append(l)

    if ''.join(ret[:len(ret)]) == ''.join(ret[::-1]):
        print('yes')
    else:
        print('no')
