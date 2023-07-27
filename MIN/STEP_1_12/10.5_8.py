def Calculator():
    score = int(input())
    if 90 <= score:
        return print('A')
    elif 80 <= score:
        return print('B')
    elif 70 <= score:
        return print('C')
    else:
        return print('D')



Calculator()

