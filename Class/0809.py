# 중복순열 >> 모든 경우의 수를 다 출력 ( 주사위 던지기

# n = list(map(int, input().split()))
# # print(n)
# path = [''] * len(n)
# def abc(level):
#     if level == len(n):
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#     for i in range(len(n)):
#         path[level] = n[i]
#         abc(level + 1)
# abc(0)




print('----------------------------------------------------')
# 중복순열 >> 모든 경우의 수를 다 출력 ( 주사위 던지기

# n = list(map(int, input().split()))
# path = [''] * len(n)
# used = [0] * len(n)
# def abc(level):
#     if level == len(n):
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#     for i in range(len(n)):
#         if used[i] == 1: continue
#         path[level] = n[i]
#         used[i] = 1
#         abc(level + 1)
#         used[i] = 0
# abc(0)
print('----------------------------------------------------')
# 순열(금, 은, 동)

#
# num = int(input())
# number = list(map(int, input().split()))
# path = [''] * num
# used = [''] * len(number)
# def abc(level):
#     if level == num:
#         for i in range(len(path)):
#             print(path[i] , end = '')
#         print()
#         return
#
#     for i in range(len(number)):
#         if used[i] == 1: continue
#         path[level] = number[i]
#         used[i] = 1
#         abc(level + 1)
#         used[i] = 0
# abc(0)

print('----------------------------------------------------')
# 조합(농구팀) . ver1
#
# n=3
# card=['A','B','C','D']
# path=[' ']*n
# used=[0]*4
#
# def abc(level):
#     if level==n:
#         for i in range(n):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(4):
#         if level > 0 and path[level -1] >= card[i]: continue
#         path[level]=card[i]
#         abc(level+1)
#
# abc(0)

print('----------------------------------------------------')
# 조합(농구팀) . ver2

n=3
card=['A','B','C','D']
path=[' ']*n
used=[0]*4

def abc(level, start):
    if level==n:
        for i in range(n):
            print(path[i],end=' ')
        print()
        return
    for i in range(start, 4):
        path[level]=card[i]
        abc(level+1, i + 1)

abc(0, 0)

print('----------------------------------------------------')
# 중복순열에서 B로 시작하는 값은 제거 . ver1

# n = 3
# path = [' '] * n
# card = ['A','B','C','D']
# def abc(level):
#     if level == n:
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#
#     for i in range(4):
#         if level == 0 and card[i] == 'B': continue   # 거르고 진입
#         path[level] = card[i]
#         abc(level + 1)
# abc(0)
print('-----------------------------------------------------')
# 중복 순열에서 B로 시작하는 값은 제거 . ver2
# n = 3
# path = [' '] * n
# card = ['A','B','C','D']
# def abc(level):
#     if level ==1 and path[level -1] == 'B' : return  # 진입 후 리턴
#     if level == n:
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = card[i]
#         abc(level + 1)
# abc(0)
print('-------------------------------------------------------')
# 중복 순열에서 같은 값이 연속으로 나오지 않는 코드 .ver1
# n = 3
# path = [' '] * n
# card = ['A','B','C','D']
# def abc(level):
#     if level == n:
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#
#     for i in range(4):
#         if level > 0 and path[level-1] == card[i] :continue
#         path[level] = card[i]
#         abc(level + 1)
# abc(0)

print('-------------------------------------------------------')
# 중복 순열에서 같은 값이 연속으로 나오지 않는 코드 .ver1
# n = 3
# path = [' '] * n
# card = ['A','B','C','D']
# def abc(level):
#     if level == n:
#         if level > 1 and path[level-1] == path[level-2]: return
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = card[i]
#         abc(level + 1)
# abc(0)

print('-------------------------------------------------------')
# # C 를 모두 제외하고 출력
# n = 3
# path = [' '] * n
# card = ['A','B','C','D']
# def abc(level):
#     if level == n:
#         for i in range(len(path)):
#             print(path[i], end = '')
#         print()
#         return
#
#     for i in range(4):
#         if card[i] == 'C' : continue
#         path[level] = card[i]
#         abc(level + 1)
# abc(0)
