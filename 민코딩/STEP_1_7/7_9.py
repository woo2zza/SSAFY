arr = list(map (int, input().split()))
count = 1
for i in arr:
    if i >= 70:
        print(f'{count}번사람은{i}점PASS')
    elif i >= 50:
        print(f'{count}번사람은{i}점RETEST')    
    else:
        print(f'{count}번사람은{i}점FAIL')  
    count += 1