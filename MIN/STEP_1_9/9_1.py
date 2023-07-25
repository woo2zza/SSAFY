arr = [4, 3 ,6 ,1 ,3 ,1 ,5, 3]
num = int(input())
count=0
for i in arr:
    if i == num:
        count += 1
print(f'숫자{num}개수는{count}개')