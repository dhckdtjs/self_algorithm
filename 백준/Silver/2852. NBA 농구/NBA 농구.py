# NBA 농구
N = int(input()) # 골 들어간 횟수
team1_list = []
team2_list = []
timem_list = []
times_list = []
# score 세기
cnt1 = 0
cnt2 = 0
for _ in range(N):
    team, time = input().split()
    time_m,time_s = time.split(':')
    time_m = int(time_m)
    time_s = int(time_s)  
    if team == '1': # team1이 득점하면 점수, 시간 기록
        cnt1+=1
        team2_list.append(cnt2)
        team1_list.append(cnt1)
        timem_list.append(time_m)
        times_list.append(time_s)
    if team == '2': # team2가 득점하면 점수, 시간 기록
        cnt2+=1
        team1_list.append(cnt1)
        team2_list.append(cnt2)
        timem_list.append(time_m)
        times_list.append(time_s)
team1_list.append(cnt1) # 최종 점수 기록
team2_list.append(cnt2)
timem_list.append(48)   # 최종 시간 기록
times_list.append(00)
victory1m = 0
victory1s = 0
victory2m = 0
victory2s = 0
for k in range(N):  # 승리 시간 기록
    if team1_list[k]>team2_list[k]:
        victory1m+=timem_list[k+1]-timem_list[k]
        victory1s+=times_list[k+1]-times_list[k]
    elif team2_list[k]>team1_list[k]:
        victory2m+=timem_list[k+1]-timem_list[k]
        victory2s+=times_list[k+1]-times_list[k]
    # 시계 규칙
    if victory1s <0:   
        victory1m-=1
        victory1s +=60
    if victory2s <0:
        victory2m -=1
        victory2s +=60  
    if victory1s>=60:
        victory1m+=1
        victory1s-=60
    if victory2s>=60:
        victory2m+=1
        victory2s-=60



# (MM:SS 출력)

print(f'{victory1m:02d}:{victory1s:02d}')
print(f'{victory2m:02d}:{victory2s:02d}') 