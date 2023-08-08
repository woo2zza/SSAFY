arr = [list(input()) for _ in range(4)]
def find(st):
    for i in range(4):
        for j in range(3):
            if arr[i][j] == st:
                return i, j
            
ret = find('A')
ret2 = find('B')
print(abs(ret2[0] - ret[0])+abs(ret2[1]-ret[1]))