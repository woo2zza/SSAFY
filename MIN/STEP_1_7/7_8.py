arr = [[3,4,1],[2,1,4],[3,3,0]]
even = 0
odd = 0
for i in arr:
    for j in i:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'짝수 : {even}')
print(f'홀수 : {odd}')