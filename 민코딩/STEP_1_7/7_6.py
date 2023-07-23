
num = list(map(int, input().split()))
for i in range(4):
    if num[i] < 20:
        print('더 큰수를 입력하세요')
    elif num[i] > 20:
        print('더 작은수를 입력하세요')
    else:
        print('정답입니다')