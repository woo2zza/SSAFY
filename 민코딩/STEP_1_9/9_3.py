arr = ['A','F','G','A','B','C']
A,B = input().split()

if A in arr and B in arr:
    print('와2개')
elif A in arr or B in arr:
    print('오1개')
else:
    print('우0개')
    