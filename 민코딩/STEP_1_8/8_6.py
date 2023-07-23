a = [[],[],[]]
def in_function():
    global a
    num = int(input())
    for i in range(3):
        arr = []
        for j in range(4):
            num += 1
            arr.append(num)
        a[i] = arr
    for k in a:
        print(*k )
    # for k in a:
    #     print(*k , end = ' ')
   

# def out_function():
#     global a
#     for i in a:
#         print(i)
    
in_function()
# out_function()