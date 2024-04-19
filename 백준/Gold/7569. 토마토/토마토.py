# 토마토

import sys
input = sys.stdin.readline
m,n,h = map(int,input().strip().split())
tomato = [[list(map(int,input().strip().split())) for _ in range(n)] for _ in range(h)]

dr = [0,0,-1,1,0,0]
dc = [1,-1,0,0,0,0]
dh = [0,0,0,0,-1,1]


from collections import deque

def bfs():
    q = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 1:
                    q.append((z,y,x,0))
    max_v = 0
    while q:
        height,row,col,cnt = q.popleft()
        max_v = max(max_v,cnt)
        for k in range(6):
            nz = height+dh[k]
            ny = row+dr[k]
            nx = col+dc[k]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = 1
                    q.append((nz,ny,nx,cnt+1))
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 0:
                    return -1
    return max_v


res = bfs()

print(res)