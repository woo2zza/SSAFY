def checkChar(i):
    if 65 <= ord(i) <= 90:
        print('대', end = '')
    elif 97 <= ord(i) <= 122:
        print('소' , end = '')



A = list(input().split())

for i in A:
    checkChar(i)

