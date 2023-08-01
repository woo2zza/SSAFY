st = list(input())
num = int(input())
st.remove(st[num])
print(*st,sep = '')