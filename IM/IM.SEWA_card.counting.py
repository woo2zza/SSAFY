T = int(input())
for q in range(1, T+1):
    card = list(input())
    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14
    for i in range(len(card) -2):
        if card[i] == 'S':
            S[int((card[i+1] + card[i+2]))] += 1
        elif card[i] == 'D':
            D[int((card[i+1] + card[i+2]))] += 1
        elif card[i] == 'H':
            H[int((card[i+1] + card[i+2]))] += 1
        elif card[i] == 'C':
            C[int((card[i+1] + card[i+2]))] += 1

    Flag = 1
    for i in range(14):
        if S[i] > 1 or D[i] > 1 or H[i] > 1 or C[i] > 1: 
            Flag = 0
            break
        else:
            Flag = 1
    if Flag: 
        print(f'#{q} {13 - sum(S)} {13 - sum(D)} {13 - sum(H)} {13 - sum(C)}')
    else:
        print('ERROR')



