num, num2 = map(int, input().split())

def in_function():
    global num
    return num + num2


def out_function():
    number = 5
    while True:
        print(number, end = ' ')
        if number == in_function():
            break
        number +=    1

out_function()

