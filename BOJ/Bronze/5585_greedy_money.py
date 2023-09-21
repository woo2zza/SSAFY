pay = int(input())
money = 1000 - pay
lst = [ 500 ,100, 50, 10 ,5 ,1 ]
cnt = 0

for i in lst:
    if money >= i:
        cnt += money // i
        money %= i
print(cnt)