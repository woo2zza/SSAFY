from collections import deque

N, K = map(int, input().split())

ret = []
dq = deque()

for i in range(1, N + 1):
    dq.append(i)

while dq:
    for i in range(K - 1):
        dq.append(dq.popleft())
    ret.append(dq.popleft())


print("<", end="")
print(", ".join(map(str, ret)), end="")
print(">")