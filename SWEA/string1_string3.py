T = int(input())
for q in range(1, T+1):
    st = list(input())
    lst = []
    while st:
        if st[-1] == 'q':
            lst.append('p')
        elif st[-1] == 'p':
            lst.append('q')
        elif st[-1] == 'd':
            lst.append('b')
        elif st[-1] == 'b':
            lst.append('d')
        st.pop()
    print(f'#{q}', end = ' ')
    print(*lst, sep = '')