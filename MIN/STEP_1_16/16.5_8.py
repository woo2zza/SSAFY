arr = [
    ['A','7','9','T','K','Q'],
    ['M','I','N','C','O','D']
]

def Flag1(st):
    Flag = False
    for i in arr:
        if st in i:
            Flag = True

    if Flag == True:
        return print(f'{st} : 존재')
    else: return print(f'{st} : 없음')

   
st1, st2 = input().split()
Flag1(st1)
Flag1(st2)