num = int(input())
def level(num):
    if num ==0:
        print(num, end = ' ')
        return
    print(num, end = ' ')
    level(num -1)
    print(num, end = ' ')
level(num)