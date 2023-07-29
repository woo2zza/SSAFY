arr= [
    ['D','A','S'],
    ['Q','W','V'],
    ['R','T','Y']
]
def Find(num1, num2):
    arr_1 = arr[num1[0]][num1[1]]
    arr_2 = arr[num2[0]][num2[1]]
    return f'{arr_1} {arr_2}'


num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
print(Find(num1, num2))