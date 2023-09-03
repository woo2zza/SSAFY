N = int(input())
people1, people2 = map(int, input().split())
rela = int(input())
arr = [[] for _ in range(N+1)]

for i in range(rela):
    st, ed = map(int, input().split())
    arr[st].append(ed)
    arr[ed].append(st)

Flag = 0
used = [0] * (N+1)
def abc(now, cnt):
    global Flag
    if now == people2:
        Flag = 1
        print(cnt)
        return 
    
    for i in arr[now]:
        if used[i] ==1 :
            continue
        used[i] = 1
        abc(i, cnt+1)        
        used[i] = 0
   
abc(people1, 0)
if Flag == 0: print(-1)