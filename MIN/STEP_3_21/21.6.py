branch, level = map(int, input().split())
count = 0
def abc(num):
    global count
    count += 1
    if num == level:
        return

    for i in range(branch):
        abc(num +1)
abc(0)
print(count)