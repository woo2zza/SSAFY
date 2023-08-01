# arr = []
# for i in range(3):
#     lst = list(input())
#     arr.append(lst)
#
# for ar in arr:
#     print(ar[-1], end = '')


print('--------------------')
arr = [ list(input())  for i in range(3)]

print(''.join(arr[-1]))