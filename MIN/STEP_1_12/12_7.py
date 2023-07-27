arrs = list(input())
for i in range(3):
    S = input()

    count = 0
    for arr in arrs:
        if arr == S:
            count += 1

  
    print(f'{S}={count}')