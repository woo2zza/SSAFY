a=int(input())

def bbq():
    global a
    if 5 > a > 0:
        print("초기값")
    elif 10 > a > 6:
        print('중간값')
    else:
        print('알수없는값')


if (a == 3) or (a == 5) or (a == 7):
    for i in range(10):
        print(i+1,end='')
elif (a == 0) or (a == 8):
    for i in range(10,0,-1):
        print(i,end='')
else:
    bbq()