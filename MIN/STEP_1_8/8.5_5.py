A,B,C = input().split()
o_A = ord(A)
o_B = ord(B)
for j in range(int(C)):
    for i in range(o_A, o_B +1):
        print(chr(i),end = '')
    print()