# 함수, Scope, 재귀함수, lambda

"""
▷ 내장 함수 = import 없이 바로 사용가능
▷ return 이 없으면 값이 'None'이 나온다

"""

print('"매개변수와 인자 예시"')
"""
def add_numbers(x, y):            # x 와 Y는 매개변수(parameter)
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b)    # a와 b는 인자(arqument)
print(sum_result)



def greet(name, age):
    print(f'안녕, {name}님! {age}살이시군요.')

greet(name = 'Dave', age = 35)

greet(age = 25, name = 'Alice')                  # 키워드로 인자를 입력시 순서가 중요하지 않음.

# greet(age = 25, 'Dave')              << Error!  키워드 인자는 위치 인자 뒤에 위치해야함
"""




'''
def func(pos1, pos2, default_arg = 'default' , *args, kwd, **kwargs):
# 위치 > 기본 > 가변 > 키워드 > 가변 키워드
'''

# Scope
"""
# local scope 함수가 만든 scope >> 함수 내부에서만 참조 가능
# global scope 코드 어디서든 참조할 수 있는 공간
def my_func():
    num = 1

print(num)      # >> num을 인식 못함
"""
# LEGB = Local << Enclosed << Global << Built-in
# 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음 (좋은 코드X)
'''
num = 100

def my_func():
    print(num)

my_func()
'''

# 예제 1
'''
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  # a = 10  c = 500
                        # b = enclosed에 없으므로 global영역의 b를 가져옴 = 2
                        # c = 500

    local(500)
    print(a, b, c)      # a = enclosed 함수 안에 있으므로 10
                        # b = enclosed 함수 안에 없으므로 global함수의 b를 가져옴 = 2
                        # c = 3

enclosed()
print(a,b)              # global 함수 안에 있으므로 a = 1
                        # b = 2
'''

# 재귀함수 ( 무한루트 조심 )
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)
'''

print('"ZIP 함수')


print('"Lambda 함수"')
'''
def addition(x , y):
    return x+ y

result = addition(3,5)
print(result)

print('-----동일 값-----')

lambda x,y : x + y
result = addition(3,5)
print(result)
'''
print('"Map + Lambda 함수 예시"')
'''
numbers = [1, 2 ,3 ,4 ,5]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [2, 4, 6, 8, 10]
'''
print('----------보 강----------')

print('▷ 함수')

print(' - 예제1')
'''
def getsum(a,b):
    return a + b , a * b    # >> python만 가능

ret = getsum(3, 5)
print(ret)
print(type(ret))
'''
print(' - 예제2')
'''
def getsum(a, b, c = 20):   # >> defult parameter 는 일반 parameter의 뒤에 사용해야한다
    return a + b + c

ret = getsum(3,5)
print(ret)
'''

print(' - 예제3')
'''
def getsum(*a):                 # >> 패킹 
    print(type(a))
    return a[0] + a[1] + a[2]   # >> 언패킹 

ret = getsum(3, 5, 1)      
print(ret)
'''
print(' - 예제4')
'''
def print_info(**A):
    print(A)
    print(type(A))
    for i, j in A.items():      # >> 딕셔너리의 key와 value를 반환하는 메서드
        print(i, j)

print_info(kevin = 1, bob = 2, john = 3)
'''
print('▷ 패킹')
'''
num = [1 ,2 ,3, 4, 5]
num2 = (1 ,2 ,3 ,4 ,5)
print(num, num2)
'''
print('▷ 언패킹')
'''
num = [1 ,2 ,3, 4, 5]
a, b, c, d, e = num
print(a, c, d)         # 언패킹 하고 남는값은 * 를 이용해서 리스트에 담을 수 있다.
a, b, *c = num
print(a, b, c)         # 1 2 [3, 4, 5]

a, *b, c = num
print(a, b, c)         # 1 [2, 3, 4] 5
'''

print('▷ 지역변수, 전역변수 scope')
'''
a = 6

def abc():
    # global a
    a = 3
    b = 5
    print(a, b)

abc()
print(a)              
'''
print(' - 예제1')

'''
def kfc():
    global a, b
    print(a, b)
    a += 1
    b += 1
    print(a, b)

def test():
    global a, b
    a = 3
    b = 3
    print(a, b)

test()
kfc()
'''
print('▷ 내장함수')
print(' - map()')
# 리스트나 튜플과 같이 순회 가능한 데이터 값에 함수를 일과적으로 적용
#   적용 후 map이라는 객체를 반환한다.
print(' - zip()')
# 순회 가능한 객체를 인자로 받고 각각의 값을 잘라서 튜플을 원소로 하는 객체 반환
'''
a = '12345'
b = 'qwert'
c = 'asdfg'

ret = zip(a,b, c)
print(list(ret))


for i in zip(a,b,c):
    print(i)

for i in zip(a,b,c):
    print(list(i))

'''
print(' - 예제1 (큐브 한면 돌리기)')
'''
arr = [[1,2,3],[4,5,6],[7,8,9]]
for i in zip(arr[0], arr[1], arr[2]):           
    print(list(i))

'''

print(' - filter')
# 리스트나 튜플같이 순회 가능한 데이터값들에 함수를 적용
# 적용 후 True 인 값만 반환하는 함수
'''
num = [1 ,2, 3 ,4 ,5 ,6, 7, 8]
# 짝수만 리스트에 담아서 출력
def get_even(value):
    if value % 2 == 0: return True
    else: return False

ret = filter(get_even, num)
print(list(ret))
'''

print(' - Lambda(익명함수)')   # 일회용 함수
'''
result = (lambda a,b : a+b)(3,5)
print(result)
'''
print(' - 예제1')
'''
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

# var1 - for문
for i in range(5):
    lst3 = lst1[i] + lst2[i]
print(*lst3)

# var2 - lambda
result = (lambda x, y : x + y)
lst3 = map(result, lst1, lst2)
print(*lst3)
'''
print('▷ 재귀함수')
'''
def abc(level):
  
    if level == 2 :
        return
    print(level, end = ' ')
    abc(level + 1)
    print(level, end = ' ')    # 0 1 1 0  >> 이해 하기.

    
abc(0)
'''