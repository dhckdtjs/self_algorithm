# 적록색약
from collections import deque
import sys
import copy
input = sys.stdin.readline
n = int(input())

dr = [0,0,-1,1]
dc = [1,-1,0,0]
def bfs(row,col,color,list):
    q = deque()
    q.append([row,col])
    list[row][col] = 0
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<n and 0<=nc<n and list[nr][nc] == color:
                q.append([nr,nc])
                list[nr][nc] = 0
    
        
paper = [list(map(str,input().strip())) for _ in range(n)]
cp_paper = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        cp_paper[r][c] = paper[r][c]
color = ['R','G','B']
cnt1 = 0
cnt2 = 0
for row in range(n):
    for col in range(n):
        for co in color:
            if cp_paper[row][col] == co:
                bfs(row,col,co,cp_paper)
                cnt1+=1
for i in range(n):
    for j in range(n):
        if paper[i][j] == 'G':
            paper[i][j] = 'R'
for row in range(n):
    for col in range(n):
        for co in color:
            if paper[row][col] == co:
                bfs(row,col,co,paper)
                cnt2+=1
print(cnt1,cnt2)
