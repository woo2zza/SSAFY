T = int(input())
for q in range(1, T+1):
    st = list(input())
    stack = []
    Flag = 1
    for i in range(len(st)):
        if st[i] == '(' or st[i] == '{':
            stack.append(st[i])
        elif st[i] == ')':
            if len(stack) == 0: 
                Flag = 0 
                break
            if stack[-1] =='(':
                stack.pop()
            elif stack[-1] == '{':
                Flag = 0
                break
        elif st[i] == '}':
            if len(stack) == 0: 
                Flag = 0 
                break
            if stack[-1] =='{':
                stack.pop()
            elif stack[-1] == '(':
                Flag = 0
                break
        
    if len(stack) == 0 and Flag == 1: 
        print(f'#{q} 1')
    else: print(f'#{q} 0')
 
 


