T = int(input())
for q in range(1, T+1):
    new_lst = []
    memory = list(input())
    if memory[0] == '1':
        new_lst.append('1')
    for i in range(1, len(memory)):
        if memory[i-1] != memory[i]:
            new_lst.append(memory[i])
    print(f'#{q}', end = ' ')
    print(len(new_lst))
