# import sys
# sys.stdin = open("input.txt","r")

# new_lst = []
# num = int(input())
# lst = list(map(int, input().split()))
# for i in range(num):
#     new_lst.insert(lst[i], i+1)

# print(*new_lst[::-1])



new = []
num = int(input())
st = list(map(int, input().split()))
for i in range(len(st)):
    new.insert(st[i], i+1)
print(new[::-1])