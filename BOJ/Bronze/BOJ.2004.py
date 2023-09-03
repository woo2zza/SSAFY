n, m = map(int, input().split())
lst =  []
Sum = 1
for i in range(1, m+1):
    Sum *= i

multi = 1
def abc(level, num):
    global multi ,Sum
    if level == m:
        number = multi//Sum
        return number
     
    multi *= num
    return abc(level +1, num-1)

ret = abc(0, n)


cnt = 0
while 1:
    if ret % 10 != 0:
        break
    else:
        ret = ret // 10
        cnt+=1
        
print(cnt)
