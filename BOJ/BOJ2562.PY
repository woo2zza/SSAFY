lst = [0] * 9
for i in range(9):
    num = int(input())
    lst[i] = num
max_lst = max(lst)
print(max_lst)
for j in range(9):
    if lst[j] == max_lst:
        print(j+1)
