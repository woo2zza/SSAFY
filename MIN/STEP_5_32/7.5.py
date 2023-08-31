arr=[list(map(int,input().split())) for _ in range(4)]
co=0

for yy in range(4):
    for xx in range(8):
        for y in range(4-yy):
            for x in range(8-xx):
                box = []
                for a in range(yy+1):
                    for b in range(xx+1):
                        box.append(arr[y+a][x+b])
                if 0 not in box and co<sum(box): co=sum(box)
print(co)