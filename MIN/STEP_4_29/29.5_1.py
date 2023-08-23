lst = [0,3,1,2,1,3,2,1,2,1,0]
st = int(input())

def abc(level):
    if lst[level] == 0:
        print('도착', end = ' ')
        return
    abc(level + lst[level])
    print(lst[level], end = ' ')
    
print('시작', end = ' ')
abc(st)
print('시작')