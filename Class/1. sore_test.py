# sort 연습

# [참고예제]
arr=['A','C','B','F','BB','G','DD','E','B','AA']
print(sorted(arr))

# 원본을 받아와 정렬한 객체로 반환
# (원본 arr 리스트 값의 순서가 바뀌지는 않음)
# 출력결과: ['A', 'AA', 'B', 'B', 'BB', 'C', 'DD', 'E', 'F', 'G']

print('---------------------------------------------------------')

arr.sort()
print(arr)

# 원본데이터가 바뀜 (원본 arr리스트 값의 순서가 바뀜)
# 출력결과: ['A', 'AA', 'B', 'B', 'BB', 'C', 'DD', 'E', 'F', 'G']

print('---------------------------------------------------------')



# 1. sorted + lambda 함수를 사용하여 아래와 같이 정렬해서 출력해 주세요 (알파벳순서대로 출력)

arr=['A','C','B','F','BB','G','DD','E','B','AA']

# 출력결과: ['A', 'AA', 'B', 'B', 'BB', 'C', 'DD', 'E', 'F', 'G']

# 1. 정답을 아래에 적어 주세요. (1번 문제는 정답을 적어 놓았음)


arr.sort()
print(arr)


# -----------------------------------------------------------------------------

# 2. 람다 함수(sorted + lambda)를 사용 하여 아래와 같이 정렬해서 출력해 주세요 (문자열길이 + 알파벳순서)

arr=['A','C','B','F','BB','G','DD','E','B','AA']

# 출력결과: ['A', 'B', 'B', 'C', 'E', 'F', 'G', 'AA', 'BB', 'DD']

# 2. 정답을 아래에 적어 주세요

sorted(arr)
print(arr)

# -----------------------------------------------------------------------------

# 3. 람다 함수를 사용하여 아래와 같이 정렬해서 출력해 주세요 (문자열길이 + 알파벳순서)

arr=['A','C','B','F','BB','G','DD','E','B','AA']

# 출력결과: ['AA', 'BB', 'DD', 'A', 'B', 'B', 'C', 'E', 'F', 'G']

# 3. 정답을 아래에 적어 주세요






# -----------------------------------------------------------------------------
# 4. 람다 함수를 사용하여 아래와 같이 정렬해서 출력해 주세요 (문자열길이 + 알파벳순서)

arr=['A','C','B','F','BB','G','DD','E','B','AA']

# 출력결과: ['G', 'F', 'E', 'C', 'B', 'B', 'A', 'DD', 'BB', 'AA']

# 4. 정답을 아래에 적어 주세요







# -----------------------------------------------------------------------------
# 5. 람다 함수를 사용하여 아래와 같이 정렬해서 출력해 주세요 (튜플의 첫번째 값을 기준으로 정렬)

arr=[(1,3),(0,3),(1,4),(1,5),(0,1),(2,4)]

# 출력결과: [(0, 3), (0, 1), (1, 3), (1, 4), (1, 5), (2, 4)]

# 5. 정답을 아래에 적어 주세요







# -----------------------------------------------------------------------------
# 6. 람다 함수를 사용하여 아래와 같이 정렬해서 출력해 주세요 ( 우선순위 1. 튜플의 첫번째 값 / 우선순위 2. 두번째 값)

arr=[(1,3),(0,3),(1,4),(1,5),(0,1),(2,4)]

# 출력결과: [(0, 1), (0, 3), (1, 3), (1, 4), (1, 5), (2, 4)]

# 6. 정답을 아래에 적어 주세요






# -----------------------------------------------------------------------------
# 7. 빈도수가 가장 많은 문자우선순위로 정렬하기
#    (단, 빈도수가 같다면 사전순으로 빠른 문자를 먼저 출력)

arr = ['A', 'B', 'Z', 'Z', 'A', 'Y', 'Y', 'Y', 'A', 'T']

# 출력결과: ['A', 'A', 'A', 'Y', 'Y', 'Y', 'Z', 'Z', 'B', 'T']

# 7. 정답을 아래에 적어 주세요






# -----------------------------------------------------------------------------
# 8. sort를 활용하여 리스트 안에 가작 작은 수(Min value) 출력하기

arr = [1, 3, 2, 4, 5, 8, 3, -2, -3]

# 출력결과: -3

# 8. 정답을 아래에 적어 주세요

print(min(arr))

# -----------------------------------------------------------------------------





