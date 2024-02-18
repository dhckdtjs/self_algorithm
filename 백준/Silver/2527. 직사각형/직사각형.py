# 직사각형
# 겹치는 부분이 직사각형이면 a, 선분이면 b, 점 이면 c , 공통 부분 없으면 d
import sys
input = sys.stdin.readline

def check_sq(st_x1,st_y1,ed_x1,ed_y1,st_x2,st_y2,ed_x2,ed_y2):
    if ed_x1<st_x2 or ed_y1<st_y2 or ed_x2<st_x1 or ed_y2<st_y1:
        result = 'd'
    elif (st_x1 == ed_x2 or st_x2 == ed_x1):
        if (ed_y1 == st_y2 or ed_y2 == st_y1):
            result = 'c'
        else:
            result = 'b'
    elif (ed_y1 == st_y2 or ed_y2 == st_y1):   
        result = 'b'
    else:
        result = 'a'
    return result

for _ in range(4):
    st_x1,st_y1,ed_x1,ed_y1,st_x2,st_y2,ed_x2,ed_y2 = map(int,input().split())
    res = check_sq(st_x1,st_y1,ed_x1,ed_y1,st_x2,st_y2,ed_x2,ed_y2)
    print(res)