from collections import deque

lst = [[3 ,7, 4] ,[2, 6 ,9],[5 ,1, 2] ,[3 ,6 ,7] ]

turn = list(map(int, input().split()))


q = deque()
q.append(lst[0][0])
q.append(lst[0][1])
q.append(lst[0][2])

remain = q.popleft()
q.append(remain)
print(q)

