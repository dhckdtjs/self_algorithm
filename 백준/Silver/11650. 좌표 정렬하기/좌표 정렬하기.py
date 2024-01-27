# 좌표 정렬하기
n = int(input())
point_list = []
for i in range(n):
    x,y = list(map(int,input().split()))
    point_list.append([x,y])
point_list.sort()
for k in point_list:
    print(k[0], k[1])