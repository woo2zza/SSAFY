import sys
sys.stdin = open("input.txt","r")
Class = int(input())
room = list(map(int, input().split()))  # 몇 개 반인지
teacher1, teacher2 = map(int, input().split())   # 총감독관, 부감독관
ret = []
cnt = 0

for i in range(Class):

    if teacher1 > room[i]:
        continue
    else:
        remain = (room[i] - teacher1) % teacher2
        if remain != 0:
            ret.append(1)

        mok = ret.append((room[i] - teacher1) // teacher2)


print(sum(ret)+Class)