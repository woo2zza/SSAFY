num = int(input())
num1 = int(input())

if num > 0 and num1 > 0: 
    print(1)
elif num > 0 and num1 < 0: 
    print(4)
elif num < 0 and num1 > 0: 
    print(2)
elif num < 0 and num1 < 0: 
    print(3)