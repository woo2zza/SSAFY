import sys
sys.stdin = open("input.txt","r")

# 소문자로만 이루어진 회원들  > 첫글자 대문자
#  대소문자 = 모두 대문자
N = int(input())
lst = []
new = []
for i in range(N):
    st = list(input())
    if ''.join(st).islower() == True:
        lst.append(''.join(st).capitalize())
    elif st[0].isupper() == True and ''.join(st[1:]).islower() == True:
        lst.append(''.join(st))
    else:
        lst.append(''.join(st).upper())

new = sorted(lst, key= lambda x : x)
for i in new:
    print(i)

