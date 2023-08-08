num = int(input())
def abc(level) :
    if level == num + 6:
        print(level, end = ' ')
        return
    abc(level +2)
    print(level, end = ' ')

abc(num)