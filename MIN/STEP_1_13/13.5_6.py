def FindABC(st1, st2):
    count_A = 0
    count_B = 0
    count_C = 0
    st3 = st1 + st2
    for i in st3:
        if i == 'A':
            count_A +=1
        elif i == 'B':
            count_B += 1
        elif i == 'C':
            count_C += 1
                
    return f'A:{count_A} \nB:{count_B} \nC:{count_C}'

st1 = list(input())
st2 = list(input())
print(FindABC(st1, st2), )

