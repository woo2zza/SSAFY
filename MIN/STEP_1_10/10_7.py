def SUM1(a, b):
    A = a + b
    return A

def GOP(a,b):
    B = a*b
    return  B


a, b = map(int, input().split())
c, d = map(int, input().split())

A = GOP(a,b)
B = SUM1(c,d)

if A > B:
    print('GOP>SUM')
elif A < B:
    print('GOP<SUM')
else :
    print('GOP==SUM')