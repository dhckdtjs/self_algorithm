# 좌표 정렬하기2
import sys
input = sys.stdin.readline
n = int(input())
point_list = []
for i in range(n):
    x,y = list(map(int,input().split()))
    point_list.append([y,x])
point_list.sort()
for k in point_list:
    print(k[1],k[0])