# 안전 영역
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
area = [list(map(int,input().split())) for _ in range(n)]           # area 받기
Max_num = 0

dr = [1,-1,0,0]
dc = [0,0,-1,1]


def bfs(row,col):                                                   # bfs
    q = deque()
    q.append([row,col])                                             # 초기값 넣기
    sink[row][col] = 3                                              # 방문처리
    while q:
        r,c = q.popleft()
        for k in range(4):                                          # 델타변환
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<n and 0<=nc<n and sink[nr][nc] == 1:           # 범위 내에 있고 아직 안 잠겼으면
                q.append([nr,nc])
                sink[nr][nc]= 3                                     # 방문처리
    
for row in range(n):
    for col in range(n):
        num = area[row][col]
        if Max_num<num:
            Max_num = num                                           # 최대값 구하기

Max_cnt = 0
for i in range(Max_num):                                            # 최대 전까지
    cnt = 0
    sink = [[1]*n for _ in range(n)]                                # 잠기는 영역 표시
    for row in range(n):
        for col in range(n):
            if area[row][col]<=i:                                   # 잠기게 되면
                sink[row][col] = 0                                  # 0으로 표시
    for row in range(n):
        for col in range(n):
            if sink[row][col] == 1:                                 # 안 잠겼으면
                bfs(row,col)                                        # bfs
                cnt+=1                                              # cnt+1
    if Max_cnt<cnt:
        Max_cnt = cnt                                               # 최대값 갱신
        if Max_cnt>cnt:
            break

print(Max_cnt)