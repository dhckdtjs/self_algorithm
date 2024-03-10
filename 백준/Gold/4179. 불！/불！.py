from collections import deque
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
maze = [list(input().rstrip()) for _ in range(R)]
fire = [[0]*C for _ in range(R)]
human = [[0]*C for _ in range(R)]

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def bfs_f():
    q_f = deque()
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'F':
                q_f.append((r,c))
                fire[r][c] = 1
    while q_f:
        row,col = q_f.popleft()
        for k in range(4):
            nr = row+dr[k]
            nc = col+dc[k]
            if 0<=nr<R and 0<=nc<C:
                if maze[nr][nc] !='#' and fire[nr][nc] ==0:
                    q_f.append((nr,nc))
                    fire[nr][nc]=fire[row][col]+1

def bfs_h():
    q_h = deque()
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'J':
                q_h.append((r,c))
                human[r][c] =1
    while q_h:
        row,col = q_h.popleft()
        if row == R-1 or row == 0 or col ==C-1 or col == 0:
            return human[row][col]
        else:
            for k in range(4):
                nr = row+dr[k]
                nc = col+dc[k]
                if 0<=nr<R and 0<=nc<C:
                    if maze[nr][nc] != '#' and human[nr][nc] == 0:
                        if fire[nr][nc] == 0 or human[row][col]+1<fire[nr][nc]:
                            q_h.append((nr,nc))
                            human[nr][nc] = human[row][col]+1
    return 'IMPOSSIBLE'


bfs_f()
res =bfs_h()
print(res)
