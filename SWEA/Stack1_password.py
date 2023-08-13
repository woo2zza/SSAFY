T = 10
for q in range(1, T+1):
    a, b = input().split()
    password = []
    for i in range(len(b)):
        # password 길이가 0 이면 초기값을 append
        if len(password) == 0: 
            password.append(b[i])
        # password 길이가 0이 아니고 password인덱스 -1값과 lst i 값이 같다면 password값 pop
        elif password[-1] == b[i]:
            password.pop()
        # password 길이가 0이 아니고 password마지막값과 lst i 값이 다르면 append
        else: password.append(b[i])
    print(f'#{q} {"".join(password)}')
