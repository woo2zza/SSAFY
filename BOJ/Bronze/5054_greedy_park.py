T = int(input())
for q in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    now = (lst[0] + lst[-1]) // 2
    store = (lst[-1] - now)*2 + (now - lst[0])*2
    print(store)
