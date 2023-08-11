arr = [
    ['A','B','C','D'],
    ['B','B','A','B'],
    ['C','B','A','C'],
    ['B','A','A','A']
]
bucket = [0] *26
arr2 = [list(input()) for _ in range(4)]
for i in range(4):
    for j in range(4):
        if arr[i][j] == arr2[i][j]:
            bucket[ord(arr[i][j])-65] +=1

Max = 0
Max_i = 0
for i in range(26):
    if Max < bucket[i]:
        Max = bucket[i]
        Max_i = i
print(chr(Max_i + 65))