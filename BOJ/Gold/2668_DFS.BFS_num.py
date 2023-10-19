# import sys
# sys.stdin = open('input.txt')

lst= []
N = int(input())
for i in range(N):
    lst.append(int(input()))

num = [i for i in range(1,N+1)]

def dfs(number):
    global result
    if number == N: 
        return result
    while 1:

        if lst[number-1] == number:
            result.append(number)

        elif dfs(lst[number-1]) == num:
            result.append(number)

        else:
            dfs(number+1)

result = []
dfs(1)
print(result)