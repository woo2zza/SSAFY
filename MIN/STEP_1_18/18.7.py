arr = [
    ['A','B','C'],
    ['A','G','H'],
    ['H','I','J'],
    ['K','A','B'],
    ['A','B','C']
]
bucket = [0] * 26
for i in range(5):
    for j in range(3):
        bucket[ord(arr[i][j])-65] += 1

for i in range(len(bucket)-1):
    bucket[i+1] = bucket[i] + bucket[i+1]

sorted_list = [0]*15
for i in range(5) :
    for j in range(3) :
        bucket[ord(arr[i][j])-65] -= 1 
        sorted_list[bucket[ord(arr[i][j])-65]] = arr[i][j]
print(*sorted_list, sep = '')