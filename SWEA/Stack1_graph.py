def abc(st, ed):
    global Flag
    if st == ed:
        Flag = 1
        return
    used[st] = 1
    for i in range(V):
        if used[i] == 1: continue
        if arr[st][i] == 1:
            # used[i] = 1
            abc(i,ed)
            used[i] = 0


T = int(input())
for q in range(1, T+1):
    V , E = map(int, input().split())
    arr = list([0]*V for _ in range(V))
    for i in range(E):
        a, b = map(int, input().split())
        arr[a-1][b-1] = 1

    s, g = map(int, input().split())

    Flag = 0
    used = [0]*V
    # used[s-1] = 1
    abc(s-1, g-1)
    print(f'#{q} {Flag}')