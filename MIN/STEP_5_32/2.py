n = int(input())
lst = []
for i in range(n):
    lst.append(list(input().split()))
    lst[i][1] =  int(lst[i][1])
    ans = sorted(lst, key=lambda x: (x[1], x[0]), reverse= True)
    for j in range(len(ans)):
        if j == 3:
            break
        print(ans[j][0], end=' ')
    print()