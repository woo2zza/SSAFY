import sys
sys.stdin = open("input.txt","r")

new_lst = []
num = int(input())
lst = list(map(int, input().split()))
for i in range(num):
    new_lst.insert(lst[i], i+1)

print(*new_lst[::-1])

# num = int(input())
# lst = list(map(int, input().split()))
# new_lst = []
# arr = [i for i in range(1,num+1)]
# for i in range(num):
#     if lst[i] == 0:
#         new_lst.append(arr[i])
#         idx = new_lst.index(arr[i])
#     elif lst[i] == 1:
#         new_lst.insert(idx-1, arr[i])
#     elif lst[i] == 2:
#         new_lst.insert(idx-2, arr[i])
#     elif lst[i] == 3:
#         new_lst.insert(idx-3, arr[i])
#     elif lst[i] == 4:
#         new_lst.insert(idx-4, arr[i])
#     elif lst[i] == 5:
#         new_lst.insert(idx-5, arr[i])
# print(*new_lst)
