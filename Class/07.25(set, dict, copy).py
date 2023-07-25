# set는 중괄호

print('▶ set_add')
'''
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)            # {1 ,2, 3, 4}

my_set.add = (4)
print(my_set)            # set에는 중복된 값 추가 x
'''
print('▶ set_clear')
'''
my_set = {1, 2, 3}       # set clear을 실행하면 ()가 나온다
my_set.clear()
print(my_set)
'''
print('▶ set_remove')
'''
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)

my_set.remove(10)
print(my_set)             # 없는 값을 제거 = KeyError   
'''

print('▶ set_discard')    # 없는 값을 제거 하고 싶을 때
'''
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

my_set.discard(10)          # .remove와 달리 에러 없음
'''

print('▶ set_pop')
'''
my_set = {1, 2, 3, 4, 5, 6}          # 정수 값 = 항상 같은 해시 값을 갖음
element = my_set.pop()

print(element)              # 1
print(my_set)               # {2, 3}


my_set = {'1', '2', '3', '4','5','6'}    # 문자 = 항상 다른 해시 값을 갖음(값이 바뀜)
element = my_set.pop()

print(element)              # 1
print(my_set)               # {2, 3}
'''
print('▶ set_update')   # 리스트형태로 추가
'''
my_set = {1, 2, 3}
my_set.update([4, 5, 1])
print(my_set)
'''
print('▶ set_집합 메서드')
'''
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}

print(set1.difference(set2))        # set1 - set2  차집합  {0 ,2 ,4}
print(set1.intersection(set2))      # set1 & set2  교집합  {1, 3}
print(set1.issubset(set2))          # set1 <= set2   False
print(set1.issuperset(set2))        # set1 >= set2   False
print(set1.union(set2))             # set1 | set2  합집합  {0 ,1 ,2 ,3 ,4 ,5 ,7 ,9}
'''

print('▶ dictionary_clear')
'''
person = {'name' : 'Alice' , 'age' : 25}
person.clear()
print(person)
'''
print('▶ dictionary_get')           # Key Error 없이 출력할 때

# person = {'name' : 'Alice' , 'age' : 25}
# print(person.get('name'))
# print(person.get('age'))
# print(person.get('country'))
# print(person.get('country', 'Unknown'))

print('▶ dictionary_삭제') 
# person.pop('kevinnnnnnnnnnnn', -1)   # pop 함수 사용해서 삭제할때 없는 키의 값을 삭제시 
#                                      # defalte parameter를 넣으면 key error를 예방할 수 있음

print('▶ dictionary_Keys, Values, Items')
'''
person = {'name' : 'Alice' , 'age' : 25}
print(person.keys())
print(person.values())
print(person.items())
'''
print('▶ dictionary_setdefault')
'''
person = {'name' : 'Alice' , 'age' : 25}
print(person.setdefault('country', 'KOREA'))   # 키와 연결된 값을 반환 / 키가 없으면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
print(person.setdefault('address'))
print(person)
'''
print('▶ dictionary_update')
'''
person = {'name' : 'Alice' , 'age' : 25}
other_person = { 'name' : 'Jane','gender' : 'Female'}

person.update(other_person)
print(person)

person.update(age = 50)
print(person)

person.update(country = 'KOREA')
print(person)
'''
print('▶ dictionary_추가, 삭제')


# st = {'Kevin' : 1, 'john' : 2, 'Bob' : 3}
# st['Kate'] = 4
# print(st)

# del st['Kate']
# print(st)

print('▶ counter class')

# # counter 클래스는 중복된 데이터가 각각 몇개씩 있는지 알려주는 클래스
# from collections import Counter
# lst = ['apple','mango','banana','apple','banana','mango','banana','apple']
# print(Counter(lst))
# ret = dict(Counter(lst))
# print(ret)

# # 문자열 중에서 가장많이 사용된 알파벳이 무엇인지 알고 싶을때 사용가능
# st = 'an applemango'
# ret2 = dict(Counter(st))
# print(Counter(st))
# print(ret2)
# print(st)

# # 가장 많이 사용된 알파벳을 출력하시오
# ret2= sorted (ret2.items(), key=lambda x:x[1], reverse = True)
# # items를 사용하면 key와 value를 튜플로 반환하는데
# # x[1] >> 즉, 알파벳 별로 사용된 개수를 기준으로 sort함

# # 알면 좋은 방법(가장 많이 사용된 물자 출력 예시)
# # Counter 라는 클래스안에 mostcommon 이라는 메서드가 있어서 그것을 예시로
# st = 'an applemango'
# ret3 = Counter(st).most_common(1)
# print(ret3)
# print(ret[0][0])

# # Counter로 문자열 덧셈과 뺄셈
# a = Counter('apple')
# b = Counter('mango')
# print(a + b)
# print(a - b)



print('▷ 예제 1')
# 혈액형 인원수 세기
# 결과 >> {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}

blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']

print('  → sol 1)')

# new_dict = {}
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재한다면,
#     if blood_type in new_dict:
#         # 기존에 키의 값을 +1 증가
#         new_dict[blood_type] += 1
#     # 키가 존재하지 않는다면 (처음 설정되는 키)
#     else:
#         new_dict[blood_type] = 1
    
# print(new_dict)


print('  → sol 2) , get')
'''
new_dict = {}
# blood_tupes을 순회하면서
for blood_type in blood_types:

    new_dict[blood_type] = new_dict.get(blood_type,0) +1

print(new_dict)
'''

print('  → sol 3) , set')

# new_dict = {}
# for blood_type in blood_types:
#     new_dict.setdefault(blood_type, 0)
#     new_dict[blood_type] += 1

# print(new_dict)

print('▶ copy')

# a = 20
# b = a
# b = 10

# print(a)    # 20
# print(b)    # 10

print('▶ slice copy')

# a = [1 ,2 ,3]
# b = a[:]
# print(a, b)         # [1, 2 ,3] [1 ,2 ,3]

# b[0] = 100
# print(a, b)         # [1, 2, 3] [100 ,2 ,3]

# c = a.copy()
# c[0] = 100
# print(a, c)         # [1 ,2 ,3][100 ,2 ,3]

# # 얕은 복사 한계
# a = [1 ,2, [1 ,2]]
# b = a[:]
# b[2][0] = 999
# print(a, b)          # [1, 2, [999, 2]] [1, 2, [999, 2]]

# c = a.copy()
# c[2][0] = 9999
# print(a, c)          # [1, 2, [9999, 2]] [1, 2, [9999, 2]]

print('▶ deep copy')
# import copy
# original_list = [1 ,2, [1 ,2]]
# deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list[2][0] = 999
# print(original_list, deep_copied_list)