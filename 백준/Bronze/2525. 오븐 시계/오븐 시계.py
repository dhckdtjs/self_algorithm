# 오븐 시계
hour,minute = map(int,input().split())
add_minute = int(input())
total_time = hour*60+minute+add_minute
new_hour = total_time//60
new_minute = total_time%60
if new_hour>=24:
    new_hour-=24
print(new_hour,new_minute)