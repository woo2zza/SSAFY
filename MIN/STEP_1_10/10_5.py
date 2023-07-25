def one():
    arr = [[9,6,3],[8,5,2],[7,4,1]]
    for i in arr:
        print(*i)

def two():
    arr2 = [[7,8,9],[4,5,6],[1,2,3]]
    for i in arr2:
        print(*i)

def three():
    arr3 = [[10, 13, 16],[11, 14, 17],[12, 15, 18]]
    for i in arr3:
        print(*i)



num = int(input())
if num % 5 ==1:
    one()
elif num % 5 == 2:
    two()
else :
    three()

