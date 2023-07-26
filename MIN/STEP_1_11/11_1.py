def in_fu():
    a,b,c = map(int, input().split())
    return calc(a,b,c)

def calc(a,b,c):
    sum = 0
    sum = a + b + c
    print(sum)


in_fu()