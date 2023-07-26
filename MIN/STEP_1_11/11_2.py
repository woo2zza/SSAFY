sum = 0
def s_fun(A,B):
    print(f'합:{A+ B}')

def m_fun(A,B):
    print(f'차:{A-B}')


a, b = map(int, input().split())
s_fun(a, b)
m_fun(a, b)
