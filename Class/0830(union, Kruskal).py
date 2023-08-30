# # 문자 2개 입력 받은 후 두 문자가 같은 그룹인지 아닌지 출력
# arr=[0]*200
# def findboss(menber):
#     global arr
#     if arr[ord(menber)]==0:
#         return menber
#     ret=findboss(arr[ord(menber)])
#     return ret
#
# def union(a,b):
#     global arr
#     fa,fb=findboss(a),findboss(b)
#     if fa==fb:
#         return
#     arr[ord(fb)]=fa
#
# union('a','b')
# union('d','e')
# union('b','e')
# union('b','d')
# union('e','f')
#
# y,x=input().split()
# # 같은 그룹인지 아닌지 출력
# if findboss(y)==findboss(x):
#     print("같은그룹")
# else:
#     print("다른그룹")

print('-----------------------------------')
print('cycle 발견 , 미발견 출력')

#
# n,m=map(int,input().split())
# edge=[]
# for _ in range(m):
#     edge.append(input().split())
# arr=[0]*200
# # cycle 발견 출력 또는 cycle 미발견 출력하기
# def findboss(m):
#     global arr
#     if arr[ord(m)]==0:
#         return m
#     ret=findboss(arr[ord(m)])
#     arr[ord(m)]=ret   # 보스찾는 경로 단축
#     return ret
#
# def union(a,b):
#     global arr
#     fa,fb=findboss(a),findboss(b)
#     if fa==fb:
#         return 1
#     arr[ord(fb)]=fa
#
# answer=0
# for i in range(m):
#     a,b=edge[i]
#     ret=union(a,b)   # 보스가 같으면 1리턴
#     if ret==1:
#         answer=1
#         break
# if answer==1:print('cycle 발견')
# else: print('cycle 미발견')


print('kruskal algo -------------------------------------------')

'''
5 8
A B 9
A C 3
A E 7
A D 20
B C 14
B D 11
C D 1
C E 5
'''

n,m=map(int,input().split())
lst=[list(input().split()) for _ in range(m)]
group=[0]*200
lst.sort(key=lambda x:int(x[2]))

def findboss(a):
    if not group[ord(a)]:
        return a
    ret=findboss(group[ord(a)])
    group[ord(a)]=ret
    return ret

def union(x,y,i):
    global group,total,cnt
    x_boss,y_boss=findboss(x),findboss(y)
    if x_boss==y_boss:
        return
    cnt+=1
    total+=int(lst[i][2])
    group[ord(y_boss)]=x_boss

total=0  # 총 공사비용
cnt=0   # 연결시킨 선의 개수

for i in range(m):
    if cnt==n-1:
        print(total)
        break
    union(lst[i][0],lst[i][1],i)