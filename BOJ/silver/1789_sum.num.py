S= int(input())
cnt = 0
Sum = 0
Flag = 0
for i in range(S+1):
    Sum += i
    cnt += 1
    if Sum > S:
        print(cnt-2)
        break
    elif Sum == S:
    
      
        print(cnt-1)
        break
