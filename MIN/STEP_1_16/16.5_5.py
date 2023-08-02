st = list(input())
a = input()
b = input()
for i in range(len(st)):
    if st[i] == a:
        st[i] = b
print(*st, sep = '')