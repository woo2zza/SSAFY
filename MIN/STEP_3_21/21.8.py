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
    elif point == 'down':
        x += directx[0] 
        y += directy[0] 
    elif point == 'right':
        x += directx[2] 
        y += directy[2] 
    elif point == 'left':
        x += directx[3] 
        y += directy[3] 

    elif point == 'click':
        print(f'{x},{y}')
