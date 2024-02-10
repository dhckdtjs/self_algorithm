# 방 배정
# 1학년부터 6학년 까지 묵을 방 배정
# 학년 별, 성별로 나눠야 함
# K만큼 인원 차면 +1
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
room_list = [0]*12                  # 학년, 성별 최대 12가지
for _ in range(N):
    gender,grade = map(int,input().split())
    for i in range(1,7):
        if grade == i:
            if gender == 0:
                room_list[2*i-2]+=1
            elif gender == 1:
                room_list[2*i-1]+=1
for k in range(12):
    if room_list[k] == 0:
        room_list[k] = 0
    elif room_list[k]>K:
        room_list[k] = (room_list[k]//K)+1
    else:
        room_list[k] = 1
Sum = 0
for room in room_list:
    Sum+=room
print(Sum)