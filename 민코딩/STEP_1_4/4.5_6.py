num = [ 3 ,9 ,12 ,15 ,55]
n1, n2, n3 = map(int, input().split())

sum = n1 + n2+ n3
if sum >10:
    print(num[-1])
else :
    print(num[0])