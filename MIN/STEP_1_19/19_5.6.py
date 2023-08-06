arr = [
    ['A','B','G','K'],
    ['T','T','A','B'],
    ['A','C','C','D']
]
def find(a2):
    count = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j] == a2[0][0] and arr[i][j+1] == a2[0][1] and arr[i+1][j] == a2[1][0] and arr[i+1][j+1] == a2[1][1]:
                count +=1
    return count

arr2 = [list(input()) for _ in range(2)]
ret = find(arr2)
if ret >= 1:
    print(f'발견({ret}개)')
else:
    print('미발견')