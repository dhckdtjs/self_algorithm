# 참외 밭
# 참외 밭은 6각형
# 면적당 참외 개수 구하기(비례식 사용)
# 동(1),서(2),남(3),북(4)
import sys
input = sys.stdin.readline
n = int(input())
width = 0
height = 0
w_idx = 0
h_idx = 0
info_list = []
cnt = 0
for i in range(6):
    direct,length = map(int,input().split())
    info_list.append([direct,length])
    if direct == 1 or direct == 2:
        if width<length:
            width=length
            w_idx = i
    else:
        if height<length:
            height = length
            h_idx = i
small_h = abs(info_list[(w_idx-1)%6][1] - info_list[(w_idx+1)%6][1])
small_w = abs(info_list[(h_idx+1)%6][1] - info_list[(h_idx-1)%6][1])
res = width*height - small_w*small_h
print(res*n)