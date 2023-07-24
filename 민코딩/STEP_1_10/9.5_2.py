str = list(input().split())
count = 0
for i in str:
    if i == 'A':
        count += 1

print(f'문자A는 {count}개발견')

for j in range(len(str)):
    if str[j] == 'A':
        print(f'{j}번')

