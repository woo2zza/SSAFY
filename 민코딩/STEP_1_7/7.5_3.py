def A():
    n1, n2 = input().split()
    return n1, n2
def B():
    n1, n2 = A()

    if 65 <= ord(n1) <= 90 and 65 <= ord(n2) <= 90:
        print('대문자들')
    elif 65 <= ord(n1) <= 90 or 65 <= ord(n2) <= 90:
        print('대소문자')
    else:
        for i in range(97,123):
            print(chr(i), end='')

B()