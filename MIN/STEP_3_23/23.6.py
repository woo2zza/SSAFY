card = list(map(int, input()))
path = [''] * 4
used = [0] * len(card)
count = 0
def abc(level):
    global count
    if level == len(path):
        count += 1
        return
    for i in range(len(card)):
        # if used[i] == 1: continue
        
        if level > 0 and abs(path[level-1] - card[i]) > 3: 
            continue
        path[level] = card[i]
        abc(level + 1)
        # used[i] = 0
        
abc(0)
print(count)