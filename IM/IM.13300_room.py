import sys
sys.stdin = open('input.txt', 'r')

import math

num, room = map(int, input().split())
room_cnt = 0
bucket_boy = [0] * 7
bucket_girl = [0] * 7
for i in range(num):
    gender, age = map(int, input().split())
    if gender == 0:
        bucket_boy[age] += 1
    if gender == 1:
        bucket_girl[age] += 1

for i in range(7):
    if 0 < bucket_boy[i] <= room:
        room_cnt += 1
    elif bucket_boy[i] != 0:
        B = int((bucket_boy[i] / room) + 0.6)   # 계산 오류 // 로 나눠주고 나머지가 있을때 if조건 추가
        room_cnt += B

    if 0 < bucket_girl[i] <= room:
        room_cnt += 1
    elif bucket_girl[i] != 0:
        A = int((bucket_girl[i] / room) + 0.6)
        room_cnt += A

# for i in range(1, 7):
#     room_cnt += math.ceil(bucket_girl[i] / room)
#     room_cnt += math.ceil(bucket_boy[i] / room)


print(room_cnt)