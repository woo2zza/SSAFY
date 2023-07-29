arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
arr4 = []
# for i in range(5):
#     arr4.append((arr1[i]*arr2[i])+arr3[i])
arr4 = [a*b+c for a,b,c in zip(arr1, arr2, arr3)]
print(*arr4, sep = ' ')
