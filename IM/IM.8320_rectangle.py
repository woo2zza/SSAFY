# import sys
# sys.stdin = open('input.txt','r')
count = 0
box = int(input())
for i in range(1, box+1):
    A = (box//i) - (i-1)
    if A > 0:
        count += A

print(count)
