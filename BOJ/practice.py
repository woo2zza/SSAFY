# import sys
# sys.stdin = open("input.txt","r")

arr = [i for i in range(ord('a'), ord('z'))]
st1 = list(input())
st2 = list(input())
lst = []
Flag = 0
path = [''] * len(st1)
def abc(level):
    global Flag
    if level == len(st1):
        lst.append(path[:])
        if st2 in lst:
            Flag = 1
        else:
            Flag = 0
        return


    for i in range(len(arr)):
        path[level] = chr(arr[i])
        abc(level +1)
abc(0)
if Flag: print('에너그램 맞음')
else:
    print('에너그램 아님')