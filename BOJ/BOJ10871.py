num, number = map(int, input().split())

a = list(map(int, input().split()))

for i in a:
    if i < number :
        print(i, end = ' ')