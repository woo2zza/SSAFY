a = int(input())
arr = [
    [[2,4],[1,5]],
    [[2,3],[3,6]],
    [[7,3],[1,5]]
]
Max = 0
Min = 100
for i in arr[a]:
    for j in i:
        if j > Max:
            Max = j
        if j < Min:
            Min = j
print(f'MAX={Max}')
print(f'MIN={Min}')