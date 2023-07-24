#문자열 관련 메소드
st = 'apple, banana, mango'

print('▷ find')
'''
index = st.find('a')   # 처음 나오는 a의 인덱스 값
index = st.find('z')   # 'z'가 없으면 -1을 반환
index = st.find('a',1) # 'z'를 1번 인덱스 이후의 값을 출력
print(index)
'''

print('▷ inupper(), inlower')
'''
print(st.upper())   #모두 대문자
print(st.lower())   #모두 소문자 판별
'''

print('▷ count')
# print(st.count('a'))  # 문자 개수 출력

print('▷ join')
# 리스트 안에 문자열 또는 문자를 하나의 문자열로 만들때 구분자 .join을 이용해서 합치기
'''
st2 = ['a','p','p','l','e']
str2 = ''.join(st2)
print(str2)

st3 = ['apple','banana','mango']
str3 = ','.join(st3)
print(str3)
'''
print('▷ upper')
'''
str2 = st.upper()
print(str2)

st = input().lower().split() # 대문자로 입력해도 소문자로 입력받기
print(st)
'''

print('▷ 공백 지우기')
'''
st2 = '  apple'
str2 = st2.lstrip() # 왼쪽 공백 제거
print(st2)
print(str2)

st3 = '  apple  '
str3 = st.strip()
print(st3)
print(str3)
'''

print('▷ replace')
'''
# lst = [1, 2, 3, 4]  lst[0] = 100    가능
# st = '  apple  '    st[3] = 'z'     불가능
st = ' apple '
str2 = st.replace('ap','pa')
print(str2)
'''

# 리스트 관련 메소드

str = ['apple','banana','mango']
print('▷ append')
'''
str.append('orange')   # 리스트에 값 추가 
print(st)
'''

'''
str.insert(1, 'orange')
print(str)
'''
print('▷ insert, extend, pop, remove')
'''
str2 = [1, 2, 3]
str3 = [4, 5]
str.extend(str2)    # >> str에 str2 추가
print(str)

str += str3         # >> str에 str3 추가
print(str)

str.pop()           # >> 마지막 값 제거
print(str)

str.remove(4)       # >> 제거 할 값을 인자값으로 넣기
print(str)

del str[3:]
print(st)

del str[1]
print(st)
'''


print('▷ reverse')
'''
str = [1, 2, 3, 4, 5]
str.reverse()
print(str)
'''

print('▷ sort (문자열 불가) - 리스트 원본 값의 위치를 변경')
'''
a1 = [6, 3, 9]
print(a1)
a1.sort()               # >> 오름차순 디폴트
print(a1)

a1.sort(reverse = True) # >> 내림차순
print(a1)
'''
print('▷ sorted (문자열 가능) - 원본값 변경x 변경된 값을 반환, 변수 지정 ex) ret')
'''
a1 = 'asdf'
a1 = sorted(a1)
print(a1)

a1 = ''.join(a1)
print(a1)

ret = sorted(a1)
print(ret)
'''

'''
lst = list(range(10))
print(lst)

ret = sorted(lst, key = lambda x:x)  # 오른차순 정렬 후 출력
print(ret)

ret1 = sorted(lst, key = lambda x:-x)                    # 리턴값에 음수 붙여서 내림차순 정렬 후 출력 (문자열은 사용 x)
ret2 = sorted(lst, key = lambda x:x, reverse = True)     # 내림차순 정렬 후 출력
print(ret1)
print(ret2)
'''
print('▷ 예제 1')
'''
lst = [(3,'banana'), (2,'apple'), (1,'carrot')]
ret = sorted(lst, key = lambda x : x[1], reverse = True)
print(ret)
'''