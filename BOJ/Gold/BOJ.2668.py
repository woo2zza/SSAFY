import sys
sys.stdin = open('input.txt','r')
# 인덱스번호 1번부터 N번까지 input값 넣어줌
N = int(input())
arr = ['']
for i in range(1,N+1):
    arr.append(int(input()))

# 결과 배열
result = []

def dfs(index, target):
    global result
# dfs를 이용해 index값과 index의 input값이 같으면 result에 넣어줌
    if arr[index] == target:
        result.append(index)
        return result
# 같지 않다면 dfs에 arr[index]를 넣어주며 index값과 같은 값이 있는지 확인
    dfs(arr[index], target)


for i in range(1,N+1):
    parents = dfs(i, i)
    if parents == i:
        result.append(parents)
print(result)