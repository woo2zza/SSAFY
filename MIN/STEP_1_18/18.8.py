train = [3, 7 ,6, 4, 2 ,9, 1, 7]
def find(team):
    Max = 0
    inx = 0
    for i in range(len(train)):
        if train[i] == team:
            Max = train[i]
            inx = i
            return inx


team = list(map(int, input().split()))
ret = []
for i in range(len(team)):
    ret.append(find(team[i]))
print(f'{min(ret)}번~{max(ret)}번 칸')