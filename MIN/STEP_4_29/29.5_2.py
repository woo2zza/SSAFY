evid = [-1,0,0,1,2,4,4]
time = [0,3,5,6,8,9,10]
st = int(input())

def abc(level):
    if evid[level] == -1:
        print('0번index(출발)')
        return
    abc(evid[level])
    print(f'{level}번index({time[level]}시)')
abc(st)