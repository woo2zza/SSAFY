# AAA ~ DDD 까지 나타내기
# arr = ['A','B','C','D']
# path = [''] * 3
#
# def abc(level):
#     if level == 3:
#         for i in range(level):
#             print(path[i], end = ' ')
#         print()
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level + 1)
#
# abc(0)

# 주사위 n개 받아서 나올수 있는 경우의수
arr = [1 ,2, 3 ,4 ,5, 6]
N = int(input())
path = ['']*N

def abc(level):

    if level == N:
        for i in range(level):
            print(path[i], end = ' ')
        print()
        return
    for i in range(6):
        path[level] = arr[i]
        abc(level + 1)

abc(0)