st1 = list(input())
st2 = list(input())

def lcs(st1, st2):
    len1, len2 = len(st1), len(st2)
    arr = [[0] * (len2+1) for _ in range(2)]

    Max = 0
    for i in range(1, len1 +1):
        for j in range(1, len2 +1):
            if st1[i-1] == st2[j-1]:
                arr[i%2][j] = arr[(i-1)%2][j-1]+1
                Max = max(Max,arr[i%2][j])
            else:
                arr[i%2][j]=0
    return Max

print(lcs(st1,st2))