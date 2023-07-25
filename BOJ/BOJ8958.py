num = int(input())

for i in range(num):
    score = 0
    sum = 0
    arr = list(input())
    for j in arr:
        if j == 'O':
            score += 1
    
        else:
            score = 0
        sum += score

    print(sum)