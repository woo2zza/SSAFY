N = int(input())
hight = list(map(int, input().split()))
result= []
for i in range(len(hight)):
    result.append(hight[i])
    for j in range(i,0 ,-1):
        if result[j-1]>result[j]:
            result[j - 1], result[j] = result[j], result[j - 1]
        else:
            break
print(result)

