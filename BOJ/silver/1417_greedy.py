N = int(input())
lst = []
cnt = 0
for i in range(N):
    people = int(input())
    lst.append(people)
while 1:

    if lst[0] == max(lst):
        break
    else:
        max(lst) - 1
        lst[0] += + 1
        cnt+=1
print(cnt)