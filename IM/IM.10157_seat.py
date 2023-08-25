C, R = map(int, input().split())
T = int(input())
arr = [[0] * R for _ in range(C)]
XY = 1
arr[0][0] = XY
dx = 0
dy = 0
idx = 0
directx = [0 ,1, 0, -1]
directy = [1 ,0 ,-1, 0]
c =0
if C * R < T :
    print(0)
else:
    while c != T-1:
        d1 = dx + directx[idx%4]
        d2 = dy + directy[idx%4]
        if d1 < 0 or d1 > C-1 or d2 > R-1 or d2 < 0 :
            idx += 1

        else:
            if arr[d1][d2] != 0 :
                idx += 1
            else:
                XY += 1
                arr[d1][d2] = XY
                dx,dy = d1,d2
                c += 1

    print(dx+1,dy+1)