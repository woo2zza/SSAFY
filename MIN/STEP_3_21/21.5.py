st = [list(input()) for _ in range(3)]
Max = -1
in_st = 0
for i in range(3):
    if len(st[i]) >= Max:
        Max = len(st[i])
        in_st = i
st[0] , st[in_st] = st[in_st], st[0]
for i in st:
    print(*i, sep = '')
