arr = [[],[],[]]
char = input()
for i in arr:
    for j in range(5):
        i.append(char)
        char = chr(ord(char) +1)
print(arr[2][2].lower())