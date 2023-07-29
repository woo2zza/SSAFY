def getName():
    A, B = input().split()
    return A,B

A, B = getName()
if A < B:
    print(A)

else:
    print(B)

