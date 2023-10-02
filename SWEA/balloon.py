T = int(input())
for q in range(1, T +1):
    st = list(input())
    ch_arr = []
    Flag = 0
    for i in range(len(st)):
        if st[i] == '(' or st[i] == '{' :
            ch_arr.append(st[i])
        elif st[i] == ')':
            if len(ch_arr) == 0: 
                Flag = 0
                break
            elif ch_arr[-1] == '(':
                ch_arr.pop()
            elif ch_arr[-1] == '{':
                Flag = 0
                break
            else:
                Flag = 1
            

            
        elif st[i] == '}':
            if len(ch_arr) == 0: 
                Flag = 0
                break
            elif ch_arr[-1] == '{':
                ch_arr.pop()
            elif ch_arr[-1] == '(':
                Flag = 0  
                break
            else:
                Flag = 1          
        if len(ch_arr) == 0:
            Flag = 1
        
    if len(ch_arr)==0 and Flag: print(f'#{q} 1')
    else:
        print(f'#{q} 0')
    