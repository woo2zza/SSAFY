# 타입, 리스트
print('진법 변경 (10진수 >> n진수')
"""
print(bin(12))
print(oct(12))
print(hex(12))

print(2/3)
print(5/3) 


# 지수 표기(제곱하는 회수) 10^
print(314e-2)  # 3.14
print(314e2)   # 31400.0


print("------")
# list 복사

lst = [1,2,3]
lst2 = lst 
# lst2가 동일한 값 lst의 주소로 할당 (lst, lst2 주소 동일)

lst = [1,2,3]
lst2 = lst[:]
# lst2가 lst의 주소를 그대로 복사  (lst, lst2 주소 다름)

lst = [[1,2][3,4]]
lst2 = lst[:]
lst[0][0] = 100
print(lst2[0][0])
# 2차원 배열은 슬라이싱해도 주소가 바뀐다.

# 해결책 >> 깊은 복사

import copy
lst = [[1,2],[3,4]]
lst2 = copy.deepcopy(lst)
lst[0][0] = 100
print(lst2[0][0])
"""
print("-----예제-----")
"""
# 1번케이스
lst=[1,2,3]
lst2=lst
lst[0]=100
print(lst2[0])

# 2번케이스
lst=[1,2,3]
lst2=lst[:]
lst[0]=100
print(lst2[0])

# 3번케이스
lst=[[1,2],[3,4]]
lst2=lst[:]
lst[0][0]=100
print(lst2[0][0])

# 4번케이스
import copy
lst=[1,2,3]
lst2=copy.deepcopy(lst)
lst[0][0]=100
print(lst2[0][0])
 
"""

print('round 함수')
'''
a = 3.14
round(a, 1)  # 소수 첫째자리까지

#math.floor 소수버리기 / 정수만 출력
'''
print('replace 함수')

print(f"오늘은 컨디션이 \"100%\" 입니다.")

lst = [1, 2, 3, 4, [5, 6, 7], 8]  #5  

print(list(range(3,8,2)))

tp = (1,2,3,4,5)
print(tp)
print(type(tp))
print(tp[-1])
print(len(tp))
print(tp[1])

di = {1:3 , 2:{4:5} , '학' : 6 , '교' : [7, 8 ,9]}
print(di)
print(type(di))
print(di[1])
print(di[2][4])
di[111] = di.pop(1)
print(di)

print('"논리연산"')
'''
a = True
b = False
c = True
d = False
print(a and b)   # a , b둘 다 맞아야 하므로 뒤에 있는 b 출력
print('' and b)  # 처음부터 틀려서 False
print(a or b)    # a , b둘 다 맞아야 하므로 앞에 있는 a 출력
print('' or b)   # a , b 두개 중 하나만 맞으면 되므로 뒤에있는 b출력
'''



print('"객체 비교하는 is"')
'''
a = 2           # integer >> 2
b = 2.0         # float >> 2
if a == b:
    print('정답')  # O
else:
    print('오답')  # X


a = 2           # integer >> 2
b = 2.0         # float >> 2.0
if a is b:
    print('정답')  # X
else:   
    print('오답')  # O
'''