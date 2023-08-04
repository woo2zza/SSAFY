arr = [
    ['C','D','A'],
    ['B','M','Z'],
    ['Q','P','O']
]
def find(st):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == st:
                return 1
    return 0

st = list(input())
plus = 0
for i in st:
    ret = find(i)
    plus += ret
print(f'{plus}명')