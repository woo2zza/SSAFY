import sys
sys.stdin = open('input.txt')

lst= []
N = int(input())
for i in range(N):
    lst.append(int(input()))

num = [i for i in range(1,8)]

def dfs(number, idx):
    global result
    while 1:
        if lst[idx] == number:
            result.append(number)
            break
        elif



result = []
for i in num:
    dfs(i)
