from collections import deque
import sys
input = sys.stdin.readline

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def bfs(row,col):
    q = deque()
    q.append([row,col,1])
    cabbage_field[row][col] = 3
    while q:
        r,c,cnt = q.popleft()
        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0<=nr<N and 0<=nc<M and cabbage_field[nr][nc] == 1:
                q.append([nr,nc,cnt+1])
                cabbage_field[nr][nc] =3
    return cnt

T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())
    cabbage_field = [[0]*M for _ in range(N)]
    for _ in range(K):
        col,row = map(int,input().split())
        cabbage_field[row][col] = 1
    worm = []
    for row in range(N):
        for col in range(M):
            if cabbage_field[row][col] ==1:
                worm.append(bfs(row,col))    
    print(len(worm))