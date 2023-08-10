st = [list(input()) for _ in range(4)]


Max = -2e50
Min = 2e50
idx = 0
def find(arr):
   Count = 0
   for i in arr:
      Count += 1
   return Count
for arr in st:
   ret = find(arr)
   if Max < ret:
      Max = ret
   if Min > ret:
      Min = ret

for i in st:
   if len(i) == Max:
      print(f'긴문장:{st.index(i)}')
for i in st:
   if len(i) == Min:
      print(f'짧은문장:{st.index(i)}')
