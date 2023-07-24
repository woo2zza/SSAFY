def BBQ(A):
    for i in range(1,A+1):
        print(i,end ='')

def KFC(B):
    for j in range(7):
        print(B, end = '')
num = int(input())
if num % 2 == 1:
    A = int(input())
    BBQ(A)
elif num % 2 == 0:
    B = input()
    KFC(B)


