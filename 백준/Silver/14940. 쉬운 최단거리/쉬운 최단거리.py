# 쉬운 최단거리
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
from collections import deque

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def find_start():
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 2:
                return r,c

def bfs(r,c):
    q = deque()
    q.append([r,c])
    while q:
        row,col = q.popleft()
        for k in range(4):
            nr = row+dr[k]
            nc = col+dc[k]
            if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[row][col]+1
                    q.append([nr,nc])



r,c = find_start()
bfs(r,c)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for l in visited:
    print(*l)

