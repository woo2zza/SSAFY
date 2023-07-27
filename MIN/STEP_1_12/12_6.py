arr = ['M','I','N','Q','U','E','S','T']

def length():
    st = input()
    for k in range(len(arr)):
        if arr[k] == st:
            return f'{st}={k}'
        
for i in range(3):
    print(length())