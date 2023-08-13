T = int(input())
for q in range(1, T+1):
    st = list(input())
    stack = []
    for i in range(len(st)):
        # 만약 stack 의 길이가 0이라면 첫글자를 append
        if len(stack) == 0: stack.append(st[i])
        # stack의 -1인덱스값이 넣으려는 값과 같다면 stack -1번을 pop
        elif stack[-1] == st[i]: stack.pop()
        # stack의 -1인덱스값이 넣으려는 값과 다르다면 append
        else: stack.append(st[i])
    print(f'#{q} {len(stack)}')
