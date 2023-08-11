arr = [
    ['A','T','B'],
    ['C','C','B']
]

arr2 = [
    ['A','A','A'],
    ['B','B','C']
]
st = input()
for i in range(1):
    if st in arr[0] or st in arr2[0]:
        print('발견')
    else:
        print('미발견')
