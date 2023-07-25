def num():
    number = int(input())
    return number

def countDown():
   
    for i in range(num(),0,-1):
        print(i, end = ' ')

countDown()