arr = ['B','D','5','Q','A']
arr2 = ['Q','E','R','E','F']
def in_function():
    a = input()
    if 65 <= ord(a) <= 90:
        print(*arr2, sep = '')
    elif 97 <= ord(a) <= 122:
        print(*arr, sep = '')
    else :
        print('HGFEDCBA')

in_function()
