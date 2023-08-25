N = int(input())
hight = list(map(int, input().split()))
result= []
for i in range(len(hight)):
    result.append(hight[i])
    for j in range(i,0 ,-1):
        if result[j-1]>result[j]:
            result[j - 1], result[j] = result[j], result[j - 1]
        else:
            break
print(result)



import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for q in range(1, T + 1):
    lst = list(map(int, input().split())) [1:]
    new_lst = []
    cnt = 0
    for i in range(len(lst)):
        new_lst.append(lst[i])
        for j in range(i,0,-1):
            if new_lst[j-1] > new_lst[j]:
                new_lst[j-1] , new_lst[j] = new_lst[j] , new_lst[j-1]
                cnt += 1
            else:
                break
    print(f'{q} {cnt}')