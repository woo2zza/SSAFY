T = int(input())
for q in range(1, T + 1):
    def page(st, ed, page):
        count = 0
        while st <= ed:
            mid = (st + ed) // 2
            count += 1
            if page == mid:
                return count
            elif page > mid: st = mid
            elif page < mid: ed = mid


    P, A, B = map(int, input().split())
    ret1 = page(1, P, A)
    ret2 = page(1, P, B)
    if ret1 == ret2:
        print(f'#{q} 0')
    elif ret1 > ret2:
        print(f'#{q} B')
    elif ret1 < ret2:
        print(f'#{q} A')
