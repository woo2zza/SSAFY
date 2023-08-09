st1 = list(input())
st2 = list(input())
st3 = list(input())
count = 0
if st1 == st2 and st2 == st3: count = 5
elif st1 != st2 and st2 != st3 and st1 != st3: count = 0
else: count = 3
if count == 5:
    print('WOW')
elif count == 3:
    print('GOOD')
else : print('BAD')