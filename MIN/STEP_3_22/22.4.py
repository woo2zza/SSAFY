st = [input() for _ in range(5)]
a = 1
for i in range(5):
    if st[i] == 'up':
        a += 1
    elif st[i] == 'down':
        a -= 1

if a <= 0:
    print(f'B{-a+1}')
else:
    print(a)