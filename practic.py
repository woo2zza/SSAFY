N, K = map(int, input().split())
lst = []
for i in range(N):
    coin = int(input())
    lst.append(coin)
lst.sort(reverse=True)
cnt = 0

for i in lst:
    if K >= i:
        cnt += 1
        K = K - i

print(cnt)
print(lst)

