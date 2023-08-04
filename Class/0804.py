# 이진 트리


# 한 배열에서 num까지만 검사해서 target이 있는지 확인
# num = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
# def binary_search(start, end, target):
#
#     while 1:
#         mid = (start + end) // 2
#         if arr[mid] == target : return 1
#         elif arr[mid] > target : end = mid - 1
#         elif arr[mid] < target : start = mid + 1
#         if start > end : return 0
#
#
# arr.sort()
# ans = binary_search(0 ,num-1, target)   # 0 >> 시작인덱스 n-1 >> arr 배열의 마지막 index
# if ans : print('찾음')
# else : print('못찾음')

# ------------------------------------------------------------------------
# parametric search

# bettery="__________"
#
# def parametric_search(st,ed):
#     Max=-1
#     while 1:
#         mid=(st+ed)//2
#         if bettery[mid]=='_':
#             ed=mid-1
#         elif bettery[mid]=='#':
#             Max=mid
#             st=mid+1
#
#         if st>ed:
#             break
#     return Max+1
# ans=parametric_search(0,9)
# print(ans*10)

#----------------------------------------------------------------------------


