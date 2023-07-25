num = int(input())
def starBox():
    for i in range(1,20,2):
        print(i, end = ' ')

def macDoll():
    for i in range(72,64,-1):
        print(chr(i), end = ' ')

def copyBean():
    for i in range(-5,6):
        print(i)


if 3500 <= num <= 5000:
    starBox()
elif 2500 <= num <= 3500:
    macDoll()
else:
    copyBean()