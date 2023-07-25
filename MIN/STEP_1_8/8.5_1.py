num = list(map(int, input().split()))
count = 0
for i in num:
    
    if i < 5:
        print(f'{count}번은 {i}점 불합격')
    else:
        print(f'{count}번은 {i}점 합격')
    count += 1

