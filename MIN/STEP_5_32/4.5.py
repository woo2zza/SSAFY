N = int(input())
arr = [3,2,-1,3,-2,10,-1]

def abc(level):
    if arr[level] == 10:
        print(f'{level}번')
        return
    abc(arr[level]+ level)
    print(f'{level}번')
abc(N)