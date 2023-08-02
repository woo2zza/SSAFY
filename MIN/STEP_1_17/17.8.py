arr = ['B','T','K','I','G','Z']
target = list(input().split())

def find(st):
    for i in arr:
        if i == st:
            return 1
    return 0

ret = 0
for i in target:
    ret += find(i)

print(ret)