st = input()
if ord(st) > 97:
    plus_shift = chr((ord(st)-65 + 3) % 26 + 65)
elif ord(st) < 65:
    mius_shift = chr((ord(st)+65 -3)% 26 - 65)
print(plus_shift,mius_shift, end ='')