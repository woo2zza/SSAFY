def pri(C, D):
    return print(C + D)

def even(A):
    ret = A * 2
    return print(ret)
    

def odd(B):
    ret = B - 10
    return print(ret)



a, b = map(int, input().split())
if ((a//b) % 2) == 0:
    integer1 = a//b
    even(integer1)
elif ((a//b) % 2) == 1:
    integer2 = a//b
    odd(integer2)

pri(a, b)
