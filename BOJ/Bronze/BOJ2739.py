A = int(input())
B = int(input())


def multi(num1, num2):
    total = 0
    for i in range(3):
        a, b = divmod(num2,10)
        print( num1 * b)
        total += (num1 * b) * 10**i
        num2 = a

    print(total)

multi(A, B)
