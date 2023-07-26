ch1, ch2 = input().split()
arr = ['D','F','G','D','A','Q']
count = 0
for i in arr:
    if ord(ch1) <= ord(i) <= ord(ch2):
        print('발견!!!')
        break
    else:
        pass
    count += 1
    if count ==6:
        print('미발견!!!')