# 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def bfs(row,col):
    q = deque()
    q.append([row,col,0])
    maze[row][col] = 3
    cnt = 1
    while q:
        r,c,cnt = q.popleft()
        if r == n-1 and c == m-1:
            return cnt+1
        else:
            for k in range(4):
                nr = r+dr[k]
                nc = c+dc[k]
                if 0<=nr<n and 0<=nc<m and maze[nr][nc] == 1:
                    q.append([nr,nc,cnt+1])
                    maze[nr][nc] = 3
n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
res = bfs(0,0)
print(res)