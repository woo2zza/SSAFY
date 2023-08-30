import sys
sys.stdin = open("../STEP_5_32/input.txt", "r")
num = int(input())
back = int(input())


for i in range(back):
    num = int(num) * 2
    num = str(num)[::-1]
print(num)

