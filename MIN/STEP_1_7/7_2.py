n1, n2 = map(int, input().split())
max_num = max(n1, n2)
min_num = min(n1, n2)

if (max_num - min_num ) % 2 == 1:
    print('고백한다')
else:
    print('짝사랑만')