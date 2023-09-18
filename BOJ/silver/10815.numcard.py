import sys
sys.stdin = open('input.txt','r')
N = int(input())
lst_N = list(map(int, input().split()))
M = int(input())
lst_M = list(map(int, input().split()))
lst_N.sort()

def binarySerach(low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if lst_N[mid] == target:
            return 1

        if lst_N[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0


for i in lst_M:
    ret = binarySerach(0,N-1,i)
    print(ret)