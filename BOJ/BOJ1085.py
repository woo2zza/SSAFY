lst = list(map(int, input().split()))


length = abs(lst[2] - lst[0])
length_2 = lst[0]
high = abs(lst[3] - lst[1])
high_2 = lst[1]

min_length = min([length, length_2, high, high_2])
print(min_length)

