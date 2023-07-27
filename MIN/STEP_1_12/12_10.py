arrs = [[0]*5 for i in range(5)]
num, st = input().split()

num = int(num)
num_st = ord(st) - 20
for x in range(5):
    for y in range(4,-1,-1):
        arrs[num-1][y] = chr(num_st)
        num_st += 1


for arr in arrs:
    for ar in arr:
        print(ar, end = '')
    print()