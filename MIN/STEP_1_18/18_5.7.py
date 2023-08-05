vect = ['M','I','N','C','O','D','I','N','G']
def find(st):
    for i in range(len(vect)):
        if st == vect[i]:
            return f'O'
    return f'X'
N = int(input())
lst = list(input().split())
for i in lst:
    ret = find(i)
    print(ret, end='')