# T = int(input())
# for q in range(1, T +1):
lst = [list(map(int, input().split())) for _ in range(9)]
Flag = 1
# for i in range(9):
#     row_Sum = 0
#     for j in range(9):
#         row_Sum += lst[i][j]
#     if row_Sum != 45:
#         Flag = 0
#         break


for i in range(9):
    col_Sum = 0
    for j in range(9):
        col_Sum += lst[j][i]
    # if col_Sum != 45:
    #     Flag = 0
print(col_Sum)
# print(f'#{q} {Flag}')
