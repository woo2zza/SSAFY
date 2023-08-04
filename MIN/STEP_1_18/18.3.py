arr = [
    [1 ,3 ,3, 5 ,1],
    [3, 6 ,2 ,4, 2],
    [1, 9, 2 ,6 ,5]
]

N = int(input())
bucket = [0] * 15
for i in range(3):
    for j in range(5):
        bucket[arr[i][j]] += 1

for i in range(len(bucket)):
    if N == bucket[i]:
        print(i, end = ' ')