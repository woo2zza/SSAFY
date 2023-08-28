
ga, se = map(int, input().split())
arr = [[0] * ga for _ in range(se)]
store = int(input())
for i in range(store):
    y, x = map(int, input().split())
    if y == 1:
        arr[0][x-1] = 1
    if y == 2:
        arr[se-1][x-1] = 1
    if y == 3:
        arr[x-1][0] = 1
    if y == 4:
        arr[x-1][ga-1] = 1

for i in arr:
    print(*i)

A =  B = C = D = 0
sty, stx = map(int, input().split())
if sty == 1:
    for i in range(ga):
        if arr[0][i-1] == 1:
            A = abs(i-stx)
        if arr[se-1][i-1] == 1:
            B = min((se + i + stx)-2, ((ga - stx)+se+(ga-i))-2)   # or   ga - i
    for j in range(se):
        if arr[j-1][0] == 1:
            C = stx + j-2
        if arr[j-1][ga-1] == 1:
            D = (ga-stx) + j -2

if sty == 2:
    for i in range(ga):
        if arr[se-1][i-1] == 1:
            A = abs(i-stx)
        if arr[0][i-1] == 1:
            B = min((se + i + stx)-3, ((ga - stx)+se+(ga-i))-2)   # or   ga - i
    for j in range(se):
        if arr[j-1][0] == 1:
            C = stx + j
        if arr[j-1][ga-1] == 1:
            D = (ga-stx) + j -2

if sty == 3:
    for i in range(ga):
        if arr[se-1][i-1] == 1:
            A = abs((ga-stx) + i)
        if arr[0][i-1] == 1:
            B = min((se + i + stx)-3, ((ga - stx)+se+(ga-i))-2)   # or   ga - i
    for j in range(se):
        if arr[j-1][0] == 1:
            C = stx + j
        if arr[j-1][ga-1] == 1:
            D = (ga-stx) + j -2
            
print(A)
print(B)
print(C)
print(D)



