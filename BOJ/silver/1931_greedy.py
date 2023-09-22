import sys
sys.stdin = open("input.txt","r")

arr = []
n = int(input())
for _ in range(n):
    arr.append((list(map(int, input().split()))))

# 파티가 끝나는 시간 기준으로 sort
arr.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0
for i in range(n):
    if end <= arr[i][0]:
        end = arr[i][1]
        cnt +=1
print(cnt)