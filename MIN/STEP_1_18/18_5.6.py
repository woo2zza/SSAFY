win = [
    [3 ,5 ,1],
    [4, 2 ,6]
]
def find(st):
    for i in range(2):
        for j in range(3):
            if win[i][j] == st:
                return f'{st}번 합격'
    return f'{st}번 불합격'

people = list(map(int, input().split()))
for i in range(len(people)):
    ret = find(people[i])
    print(ret)