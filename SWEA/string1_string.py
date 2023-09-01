T = int(input())
for q in range(1, T+1):
    st = input()
    st2 = input()
    Flag = 0
    if st in st2:
        Flag = 1
    print(f'#{q}',end = ' ')
    if Flag: print(1)
    else: print(0)