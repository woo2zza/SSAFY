# import sys
# sys.stdin = open('input.txt','r')

arr1 = []
arr2 = []
ga, se = map(int, input().split())
num = int(input())
for i in range(num):
    sun, cut = map(int, input().split())
    if sun % 2 == 0:
        arr1.append(cut)
    elif sun % 2 ==1:
        arr2.append(cut)

arr1.append(se)
arr2.append(ga)
arr1.sort()
arr2.sort()
ga_Max = 0
se_Max = 0
for i in range(len(arr1) -1):
    if arr1[i+1] - arr1[i] > ga_Max:
        ga_Max = arr1[i+1] - arr1[i]
for i in range(len(arr2) -1):
    if arr2[i+1] - arr2[i] > se_Max:
        se_Max = arr2[i+1] - arr2[i]

print(ga_Max * se_Max)