# 안전 영역
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
area = [list(map(int,input().split())) for _ in range(n)]
Max_num = 0

dr = [1,-1,0,0]
dc = [0,0,-1,1]


def bfs(row,col):
    q = deque()
    q.append([row,col])
    sink[row][col] = 3
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<n and 0<=nc<n and sink[nr][nc] == 1:
                q.append([nr,nc])
                sink[nr][nc]= 3
    
for row in range(n):
    for col in range(n):
        num = area[row][col]
        if Max_num<num:
            Max_num = num

Max_cnt = 0
for i in range(Max_num):
    cnt = 0
    sink = [[1]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if area[row][col]<=i:
                sink[row][col] = 0
    for row in range(n):
        for col in range(n):
            if sink[row][col] == 1:
                bfs(row,col)
                cnt+=1
    if Max_cnt<cnt:
        Max_cnt = cnt

print(Max_cnt)