# 토마토
from collections import deque
M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
dr = [0,0,-1,1]
dc = [1,-1,0,0]
def bfs():
    q = deque()
    cnt = 0
    for row in range(N):
        for col in range(M):
            if tomato[row][col] == 1:
                q.append((row,col,0))
    while q:
        r,c,cnt = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<N and 0<=nc<M:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = 1
                    q.append((nr,nc,cnt+1))
    return cnt
res = bfs()
for rr in tomato:
    if 0 in rr:
        res = -1
        break
print(res)
