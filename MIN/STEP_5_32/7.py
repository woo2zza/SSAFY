import sys
sys.stdin = open("input.txt","r")
N = int(input())
arr = [[0]*3 for _ in range(3)]
for i in range(N):
    A, B, C = map(int, input().split())
    arr[A][B] = C

K = int(input())
lst = list(map(int, input().split()))


