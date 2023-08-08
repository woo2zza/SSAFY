directx = [1,-1,0,0]
directy = [0,0,1,-1]

x,y = 5,5
dx = 0
dy = 0
num = int(input())
for i in range(num):
    point = input()
    if point == 'up':
        
        x += directx[1] 
        y += directy[1] 
        dx = directx[1] + x
        dy = directy[1] + y
    elif point == 'down':
        dx = directx[0] + x
        dy = directy[0] + y
    elif point == 'right':
        dx = directx[2] + x
        dy = directy[2] + y
    elif point == 'left':
        dx = directx[3] + x
        dy = directy[3] + y

    elif point == 'click':
        print(f'{x},{y}')
